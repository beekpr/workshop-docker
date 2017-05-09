# Part 5

In part 3 of the exercise we created a stack composing of a load balancer (nginx), a stateless app (counter-app) and a redis backend store. At this point, you should feel the pain of setting up multiple containers and linking them.

## Docker-compose

Docker compose is a tool build around docker to orchestrate multiple containers and start these. Docker-compose uses a single YAML file called `docker-compose.yml` to define all the services required. 
The format is very similar to the docker commands which were already running.

### Docker compose file

An example docker compose file looks like:

```
version: '2'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: "redis"
```


### Starting the Stack
To bring up the entire stack, you simply type

```
docker-compose up
```

if you want the stack to run in the background, use the -d flag

```
docker-compose up -d
```

### Stopping the Stack

Simply type

```
docker-compose down
```

to stop the stack

## The Exercise

Create a docker compose file for your stack
