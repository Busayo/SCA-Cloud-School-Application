# SCA-Cloud-School-Application

Link to my docker hub repository

https://hub.docker.com/repository/docker/busayo00/test 




TESTING AND OUTPUT PROCESS
Test the root directory, I ran "docker build --tag test ." to build the image

Then I ran "docker run -p 5000:5000 test:latest" to run the application 

To test my application on my browser, I went to localhost:5000

(insert picture)



INSTRUCTIONS 
The name of my account on dockerhub is "busayo00" and the repository I created is called "test"
On my command line, I ran docker login and inputed my credentials to authenticate my docker user on my laptop 
I ran "docker tag test:latest busayo00/test:latest"
Then I ran, "docker push busayo00/test:latest" 

Docker Repository : https://hub.docker.com/repository/docker/busayo00/test




DOCUMENTATIONS USED FOR DEPLOYMENT
I made use of the following resources during the course of this project

https://hub.docker.com/r/busayo00/test/tags 

https://docs.docker.com/engine/reference/builder/

https://www.pluralsight.com/guides/create-docker-images-docker-hub

https://www.exquisappfactory.com/2020/01/31/introduction-to-containers-and-docker/

https://www.geeksforgeeks.org/dockerize-your-flask-app/

https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/

https://geekflare.com/understanding-docker-for-beginner/







