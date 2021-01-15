# SCA-Cloud-School-Application

Link to my docker hub repository

https://hub.docker.com/repository/docker/busayo00/test 




TESTING AND OUTPUT PROCESS



Inside the root directory, I ran "docker build --tag test ." to build the image

Then I ran "docker run -p 5000:5000 test:latest" to run the application 

![1image](https://user-images.githubusercontent.com/17340292/104752273-c478ff00-5756-11eb-8a7a-1e256bf9b751.jpg)





To test my application on my browser, I went to localhost:5000

![2image](https://user-images.githubusercontent.com/17340292/104752437-f1c5ad00-5756-11eb-8c33-9d3ead98438d.jpg)



INSTRUCTIONS 



The name of my account on dockerhub is "busayo00" and the repository I created is called "test"
On my command line, I ran docker login and inputed my credentials to authenticate my docker user on my laptop 
I ran "docker tag test:latest busayo00/test:latest"
Then I ran, "docker push busayo00/test:latest" 

To pull the docker image back to my local system in case of an update, I ran "docker pull busayo00/test:latest"

![3image](https://user-images.githubusercontent.com/17340292/104753919-e83d4480-5758-11eb-9525-308a64dc8f1d.jpg)

and then to run it on my local system, I ran "docker run -it busayo00/test:latest"

![4image](https://user-images.githubusercontent.com/17340292/104754265-4f5af900-5759-11eb-95f2-c87c6555e403.jpg)

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







