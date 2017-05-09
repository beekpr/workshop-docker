# Part 4

In Part 3, you saw how you could combine multiple containers together to begin building a scalable service. In this part we want to use the containers published by the other workshop participants to power our service.

Firstly if you haven't already please sign-up for a GitHub account and create a repository for your amazing counter application. Now that we have a home for our application wouldn't it be amazing if every time we pushed a new change the docker image would be built automatically for us? Well it is actually really easy.

1. Visit hub.docker.com, signup for a new account and then navigate to the settings to link your GitHub account.
2. Next click Create on top right menu and select Create Automated Build
3. Select your GitHub account and repository
4. Enter docker repository name and description
5. Navigate to Build Settings and update branches and Dockerfile location if different
6. Lastly trigger a manual build (if you have already pushed your code to GitHub) otherwise push to build automatically.

If the build succeeds post your docker pull command on the workshop app (https://workshop-docker-eth.beekeeper.io/stream/general).

Now for the fun part, see if you can replace your counter app with one of the other docker images posted to stream. If it is built to specification it should just work :)
