# BankNote_Authentication
Using Flask and Swagger API, docker for containerizing the project, and heroku for wep api its an end to end application for bank note authentication

I have creaed a https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/classifier_bankNote_authentication.pkl 
model which is based on Random Forest Classifier. It has used a dataset from kaggle. An API using flask and swagger is used 
https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/flask_api_bankNote_authentication.py. While implementing
this api on the server it can be accessed throgh and ip address as 0.0.0.0:8000/apidocs/. And Further I had build and web API using heroku
to this link https://banknote-authentication-api.herokuapp.com/
In this you can execute the program through the get and post request both as seen in the figure below:
1) This is the landing page of banknote authetication api

![Test Image 1](https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/screenshot/landing_page.png)

2) This is the get request page of banknote authetication api

![Test Image 1](https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/screenshot/get_1.png)
![Test Image 1](https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/screenshot/get_2.png)

3) This is the post request page of banknote authetication api

![Test Image 1](https://github.com/KrishnaRauniyar/BankNote_Authentication/blob/main/screenshot/post.png)


Further more I have containarized my api with the anaconda base image.
