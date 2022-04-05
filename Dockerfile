FROM jupyter/minimal-notebook

WORKDIR /ctt_app

RUN git clone https://github.com/nycdsaluke/pkg_ctt.git

RUN pip install -e ./pkg_ctt

RUN mkdir ./monitor
RUN mkdir ./monitor/myvolume

COPY ./program_template ./monitor/program_template
COPY ./README.md ./monitor/README.md

WORKDIR monitor

EXPOSE 8888


CMD ["jupyter", "notebook", "--ip='*'",  "--NotebookApp.token=''", "--NotebookApp.password=''"]
