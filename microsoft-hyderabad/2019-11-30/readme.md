# Python Django Session at Microsoft Hyderabad...

Follow following steps
1. First of all create a folder.
2. Create virtual environment
	
	1. For windows, you can use following command
		```bash
		py -m venv <EnvironmentName> 
		```
	2. For macOS and Linux, you can use following command
		```bash
		python3 -m venv <EnvironmentName> 
		```
	**Note**
	If you are using Python 2, replace venv with virtualenv in the below commands.
	
3. Now after creating virtual environment, you need to activate it. 
	
	1.  For Windows run this in command prompt
		```bash
		.\env\Scripts\activate
		```
	2.  For macOS and Linux:
		
		```bash
		source env/bin/activate
		```
4. Now install django, To install the Django you can use following command
```bash
	pip install django
```

5. Now create the project to Create the project you can use following command
```bash
	django-admin startproject sampleproject
```

6. Now your project is create you can check settings.py, manage.py and urls.py file as we discussed in the session.

7. Now to run your project. You can use following command
```bash
py manage.py runserver
```

	**Note** 
when you will run your project automatially **db.sqlite3** file will be generated.

8. Now create **views.py** file and write following code.
```python
from django.http import HttpResponse
#Function which we will call from the urls.py
def welcome(request):
    return HttpResponse("Hello World")
```
9. Now in **urls.py** file write the following code.
```python 
from django.contrib import admin
from django.conf.urls import url,include
from .views import welcome
# Now you can provide urls accordingly
urlpatterns = [
    	url('admin/', admin.site.urls),
    	url(r'^welcome$',welcome)
		url(r'^$',welcome)  # if you want to create home page url then you can use this becuase home page will you error that's why I added this
]
```
---
## Migration

When we run the our application then we get warning that we have n number of the migrations pending, that is database related  changes which comes with existinginstalled  application. I am just writing the commands for the migrations which we have already discussed.

```bash
py manage.py showmigrations
py manage.py sqlmigrate
py manage.py migrate
```
---
## Admin page 

You can open admin page now using /admin

---

## Create Super User

To login into the system you have to create the super user to create the super user you can fire following command in the shell 

```bash
py manage.py createsuperuser
```
---

## Creating the application for your project

As we discussed in the session that we can attach multiple application to the project so first we will create it and then we will attach that.

You can follow following steps to work on the application

1. Create the app using following command
```bash
py manage.py startapp newapp
```
2. Go to your model.py file and add Model Class (You can use following code)
```python
class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    Contact_Number=models.CharField(max_length=15, blank=True)
```
3. attach your app to the project for that go to your **settings.py** file of the project and add your application name in the list(Array) **INSTALLED_APPS**(That is new app which we have created)
```python
INSTALLED_APPS = [
		'newapp',
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
]
```
4. After adding your model should be update to database so steps are as follows
	1. Make the migrations
	2. Check your migrations in sql format
	3. Show your migrations in command prompt 
	4. migrate to the database
	
	To perform all the steps you can follow, following steps
	```bash 
	py manage.py makemigrations
	py manage.py sqlmigrate newapp 0001
	py manage.py showmigrations
	py manage.py migrate
	```
---
## Register your application to admin page for that I am just providing code which you can update in **admin.py** file of your app.

**Code for admin.py**
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Email = models.CharField(max_length=100, blank=False)
    Contact_Number=models.CharField(max_length=15, blank=True)

    def __str__(self):
        return "{0} {1} {2}".format(
            self.Name,
            self.Email,
            self.Contact_Number
        )
```

---

## Resources
[Download Python](https://www.python.org/downloads/ "Download Python")

[Sqlite database open online](https://sqliteonline.com/ "Sqlite database open online")

**For more question you can ask here**

[My Website](https://www.sourabhsomani.com/ "My Website")

[sourabh_somani2010@hotmail.com](mailto:sourabh_somani2010@hotmail.com?Subject=Hello%20Sourabh "sourabh_somani2010@hotmail.com")

[Twitter](https://twitter.com/sourabh_somani "Twitter")

[Linkedin](https://www.linkedin.com/in/sourabhsomani/ "Linkedin")

[Instagram](https://www.instagram.com/sourabhsomani8/ "Instagram")

[Facebook](https://www.facebook.com/hackersourabh "Facebook")

Thank You :)
