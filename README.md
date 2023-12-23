# Task-2-RESTful-API-Development
1. Django: Implement a minimal Django REST framework API for managing a collection of items (e.g., books, movies).  2. Include endpoints for retrieving all items and adding a new item.

#step to run this project
1. Open this folder in Visual Studio Code or Pycharm
2. Open a terminal or command prompt and navigate to the directory where your Django project is located.
     cd path/project 
4. install the necessary packages that are used in this project. Run the below commands in terminal to install packages
   pip install django
   pip install djangorestframework
5. perform the migration by running the below command in cmd
   python manage.py migrate
7. to run the this project run the below command
   python manage.py runserver
8. Open your web browser and go to http://127.0.0.1:8000/bookapi/ 
9. this will open the browser where you can add the item by entering the name and description.
10. and if you click on the get button it will shows all the item which are there in the table
