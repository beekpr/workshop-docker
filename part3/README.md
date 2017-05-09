# Part 3

In Part 2, you have build your own dockerized service which works with a backend. Now we want to scale it up and run 3 instances.

## Running 3 instances

To run three instances of your app, simply call docker 3 times:

```
docker run --name="counter-1" -d workshop/counter-app
docker run --name="counter-2" -d workshop/counter-app
docker run --name="counter-3" -d workshop/counter-app
```

Every one of these apps is running its own instance.

## Load balancing

To load balance between the containers, we can use nginx. To simplify things, we have provided the nginx.conf configuration which you can use immediately to load balance between the nodes. You can find nginx on dockerhub

The configuration is visible under resources/nginx/nginx.conf

Now you can start and stop containers, but your website will remain working