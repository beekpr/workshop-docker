# Introduction

This is a workshop to learn how to use docker

## Before we begin...

First, install the docker engine on your local machine. Detailed instructions on how to install docker on any platform can be found under https://docs.docker.com/engine/installation/

# Part 1

This part of the workshop shows how to build a docker image as well as run a container from that image

## Building a docker image for a sample application

In the first step, you will learn how to build and run a sample application. Go to the folder resources/counter-app-in-memory

This is a simple web application written in python which displays the amount of times a web site was opened. To build the docker image, navigate to the counter-app-in-memory folder (`cd resources/counter-app-in-memory`) and build the image via:

```
docker build .
```

The last line of the output should look more or less like this:

```
Successfully built XXXXX
```

By default, docker randomly generates a name.


## Running your first app

You can run now

```
docker run XXXXX
```

where XXXXX is the image name from the previous command.

Try to access the URL `localhost:5000` from your browser.

You will see that it will not work. This is because the container runs in an isolated environment, and does not bind to the local machines port. To bind the containers port to the host port, run the following command:

```
docker run -p 5000:5000 XXXX
```

Now you can access the simple flask application over `localhost:5000`


## Modifying your first app

Currently the app will output:

> You have accessed this website 1 times

in the beginning. This is a gramatical error, and we would like to fix it, so that if the count is 1, we display:

> You have accessed this website 1 time

To do modify `main.py` which the appropriate changes.


Notice that if you rerun the application, it still shows the old version. This is because the container has its own copy of the file. 

We can now run `docker build .` to rebuild the application. Note that the image id will change, because it will be a new image

To make development life even easier, we can also mount the src directory into the container, so that it uses the local files instead of the files in the container. In that case, we will actually not have to rebuild the container anymore!

```
docker run -p 5000:5000 -v src:/opt/counter/src XXXX
```

## Running in the background

You can also run the app in the backgroud by using the -d flag

```
docker run -d -p 5000:5000 -v src:/opt/counter/src XXXX
```

## Finding the running container

Type in `docker ps` to find the running docker containers

You can stop containers with `docker stop` and remove containers with `docker rm`

## Giving the image a useful name

You may have noticed that it is not very useful to have random names for the images. We can now build the image with a useful name in mind. You can do it with the `--tag` flag. E.g.

```
docker build --tag="<owner>/<name>[:<version>]" .
```

The name consists of an owner, an app name and an optional version. Official images skip the owner (e.g. ubuntu). The version is optional. If the version is ommited, then "latest" is used as a version.

E.g., use

```
docker build --tag="eth-workshop/counter-in-memory:1" .
```

Now you can use `eth-workshop/counter-in-memory` in every place you used XXXX before.