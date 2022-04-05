# README

## Build an image

The image can be built with 

``docker built -t <image_name> .``

## Initialize a container

Once done building, one can spin up a container with the command below:

``docker run -d --rm -p <port>:8888 -v <full_path>:/ctt_app/monitor/myvolume <image_name>``

This way the container will run behind the scene.

## Use the container

To access the container, one can search ``localhost:<port>`` in teh browser. The placeholder `<port>` is the port your chose when initialize the container.

This command should bring the user to a jupyter notebook where three folders are shown:
