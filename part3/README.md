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