
## **Storefront3**

The api of an Ecommerce website with Django Rest Framework.I did this project in the Mosh Hamedani Django series course(last section) in codewithmosh.com.

## **Introduction**

this project completes the (https://github.com/MSIZ47/storefront2) project.we have some changes in the models(products have image now).I add uploading files,sending templated emails,running background tasks and automated and performance
testing to the project as well as caching and logging.In fact, it is ready for production

##  **Description**
In this project i did the api with ModelViewSet, Serializers and Routers.i used advanced approach to do api such as mixins and nested routers too.i did the authentication with Djoser using json
web token authentication. and permissions with custom and model permissions of DRF.i covered filtering,searching,sorting and pagintion of api with DRF too.i simulate a signal for creating a customer
record in database when someone registers to get familiar with signals and custom signals.i managed images in the admin.i used fake smtp server for sending templated emails.I simulate some background tasks and 
managed them with celery and redis.on the other hand,i used flower for monitoring celery tasks.I did performance testing for this project using Locust and profiling with Silk.I got familiare with stress testing too.
I used Redis for caching, then i simiulate a slow api and verify optimization with caching.At last i configured logging and then served the application with gunicorn.

## **Installation**

To install Project Title, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: **pipenv install**
4. activate virtual env :  **pipenv shell**
5. create a mysql database called storefront3
6. migration in the project --> 1:**python manage.py makemigrations**, 2:**python manage.py migrate**
7. create some fake data if you want(you can use the *sead.db* in the project) for better undrestanding of the API
8. Start the project: **python manage.py runserver**

## **Usage**

follow these steps:

1. Open the project in your favorite code editor.
2. Modify the source code to fit your needs.
3. start the project: **python manage.py runserver**
4. Use the project as desired.



## **Conclusion**

The api of an Ecommerce website with advanced concepts of DRF.I learned some advance hints and tools for DRF with **STOREFRONT3** Project and I did my best to practice  DRF completing this project.In (https://github.com/MSIZ47/Bookstore-DjangoRESTframework-)
project i tried to complete the api of an bookstore and add some new things to it,So please have a look on that next.
