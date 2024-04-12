# Python Recipe Application

## Description

### In this application I am using python to create a recipe application for people to be able to add recipes and keep track of them. It alows people to login, search through recipes, use data visualization, add recipes, and logout. It is a simple application created to show skills using Django, Python, SQLite, HTML, CSS, and Heroku. 

## Instalation

1. Clone the repository

```git clone git@github.com:MitchellDLandau/A2_Recipe_App.git```

2. Install all dependencies for the application

```pip install -r requirements.txt```

3. Setup the database locally

```Configure the database settings in 'settings.py' for SQLite```

```python manage.py makemigrations```

```python manage.py migrate```

4. Create a superuser for yourself to run the database

```python manage.py createsuperuser```

5. Run the server 

```python manage.py runserver```

6. Access the website and test

Open your browser to the adress provided when previos command was entered, it should be something like 'http://127.0.0.1:8000'.

## Technologies Used

* Django
* Python
* JavaScript
* SQLite
* Heroku
* HTML/CSS
