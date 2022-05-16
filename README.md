# Description

this program creates an api of that uses a mysql database to make http request to GET POST PUT and DELETE infotmation on said database .
It uses face recognition to validate the person in the picture

# Dependencies

To be able to try the program, you need ..

To install an Integrated development environment(we used visual studio code code for this one(best IDE so far in my opinion)).

You also need to install the latest version of python, face_recognition, django framework, dlib, os adn cv2 .



# How to use

-To use the api , you ll need to use postman or the base django site to test the api calls.

-Sadly my heroku account is dissable at this time so we can only test this locally 

-Some api calls you can try are http://127.0.0.1:8000/employees/
to get the the employes and their facial keypoints.

-sadly i wasnt able to connect an api call to my fae recognition but it does work . i have set uo multiple pictures of the coaches . if we run the program it will find the right person. 

# Deployment of the api

-The api was deployed using heroku. 

-To deploy you need to download the heroku cli then use the command to set up a remote git repository

-from there 
-we git add .

-we git commmit

-and finally we git push heroku main

-sadly my deployment stopped working