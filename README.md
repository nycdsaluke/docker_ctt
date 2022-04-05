## README

### Build an image

The image can be built with 

``docker built -t <image_name> .``

### Initialize a container

Once done building, the coordinator can spin up a container with the command below:

``docker run -d --rm -p <port>:8888 -v <full_path_volume>:/ctt_app/monitor/myvolume <image_name>``

This way the container will run behind the scene.

### Use the container

To access the container, the coordinator can search ``localhost:<port>`` in teh browser. The placeholder `<port>` is the port the coordinator chose when initialized the container.

This command should bring the coordinator to a jupyter notebook where three folders are shown:

- myvolume
- program_template
- README.md (the file you are reading)
- create_program_folder.ipynb

The logic is to create a folder by running the short script in `create_program_folder.ipynb` for each program. Such a folder will be a copy of `program_template` in `myvolume`, which is the folder inside the container that is mount with <full_path_volume> the coordinator specified when spinned up the container.

Inside the program folder, place the Google API credentials to the `coordinator_creds` and fill in the blank in `config.yaml`. Then go to `main.ipynb` for monitoring.
