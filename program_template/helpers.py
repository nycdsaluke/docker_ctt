import yaml
from ctt.gapi.drive_io import get_df_from_sheet
from ctt.mngmnt_utils.mentor_report import collect_reports_of_the_week
from ctt.mngmnt_utils.reminder import send_reminder
from ctt.mngmnt_utils.report2mngr import format_report2mnger


config_path = 'config.yaml'

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)


cred_path = config["coordinator"]["cred_path"]
mentor_student_sheet_id = config["mentor_student_sheet_id"]
mentor_sheet_id = config["mentor_sheet_id"]

mentor_students = get_df_from_sheet(cred_path, mentor_student_sheet_id)
mentors = get_df_from_sheet(cred_path, mentor_sheet_id)


def collect_weekly_report(target_date):
    return collect_reports_of_the_week(mentor_students, target_date, cred_path)


def aggregate_missing(reports, mentors):
    missing = reports.groupby("student").agg(
        missing = ("Timestamp", lambda t: t.isnull().all()),
        mentor = ("mentor", "first"),
        form_url = ("form_url", "first")
    ).reset_index().merge(
        mentors
    ).rename(columns={"email":"mentor_email"})
    missing = missing.loc[
        missing["missing"],
        ["student", "mentor", "mentor_email", "form_url"]
    ]
    return missing.values.tolist()


def send_reminder_to_mentors(missing, target_date):
    send_reminder(missing, config, target_date, cred_path)


def create_html_report_to_client(reports, topic, target_date):
    report_dir = config["report"]["dir"]
    format_report2mnger(
        reports, config, topic, target_date, report2mngr_dir=report_dir)