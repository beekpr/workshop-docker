# Part 2

In this part, we will launch a more complex application, which consists of multiple services

In Part 1, we used an application which would count the amount of time a person visited the website. It turned out, that the website went viral, and we are having a lot of traffic.

To ensure that we can handle the amount of traffic coming it, we need to be able to scale our services to more than just 1 container running.

This is currently not possible with the implementation from part 1, since the application keeps the number of visits in memory. If we spread this over multiple containers, every container will have a different number.

## Getting a data store

Firstly, we need to find a data store. For this exercise, we decided to use **redis** as a very simple storage backend. First we need to be able to run redis on our machine. To do this, we can use docker. A lot of the common services are already "dockerized", meaning that docker images for these exists. These are usually stored on dockerhub. Dockerhub can be accessed via `https://hub.docker.com/`

Find redis on dockerhub and run version 3.0 on your machine


## Build your own app

Now it is time to get your hands dirty. Build an app (pick your favourite technology!!! e.g. JavaScript, java, python, ruby...) and connect to the redis instance running on your local machine.

The service should behave exactly like the service in part 1, but with the exception that it talks to redis and stores the data in there. The service should work in the following way:

 1) Every time somebody accesses the website, the current timestamp as an ISO 8601 string with UTZ timezone. E.g. `2017-05-09T11:53:57Z`, is `rpushed` on the list stored at key `visits`
 2) The application takes the `llen` of the list stored at key `visits` and displays this as the amount of visits

## Dockerize your app

Now you should have an app in your favourite technology stack which runs with the redis backend. We now need to dockerize your app. To do that, create a Dockerfile and add your steps there. You can use environment variables to configure the app with parameters. Running the container with -e VAR=VALUE will run it with a given environment variable. This is how you can pass in configuration parameters