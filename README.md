# 05_heroku_app

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

https://nano-proj5.herokuapp.com/

## Motivation for developing this project

I have developed this project as I am a software engineer looking to broaden knowledge across the stack and gain skills to aid projects that I work on in my day job.

I developed this project specifically to make use of the knowledge I have acquired across the Udacity Nanodegree and gain confidence in consolidating these skills.

Further it has been great to schedule more time into development and share my work in the open-source community.

# Set Up
## Installing Dependencies
```
Python 3.8.12
```
Follow instructions to install the correct version of Python for your platform
in the python docs.

## Virtual Environment (venv)
We recommend working within a virtual environment whenever using Python for
projects. This keeps your dependencies for each project separate and organaized.
Instructions for setting up a virual enviornment for your platform can be found
in the python docs.
```
python -m venv venv
venv/bin/activate
```
## PIP Dependecies
Once you have your venv setup and running, install dependencies by navigating
to the root directory and running:
```
 pip install -r requirements.txt
 ```
This will install all of the required packages included in the requirements.txt
file.

## Accessing local env variables
To access local environment variable run the below command, feel free to update these variables to suit your set up:
```
source setup.sh
```

## Local Database Setup
Once you create the database, open your terminal, navigate to the root folder, and run:
```
python manage.py db init
python manage.py db migrate -m "Initial migration."
python manage.py db upgrade
```
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.


## Local Testing
To test your local installation, run the following command from the root folder:
```
python ./test_app.py
```
If all tests pass, your local installation is set up correctly.

## Running the server
From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```
python app.py
```
Debug model is already set to true in the app:
```
if __name__ == '__main__':
    app.debug = True
    app.run()
```
The application will locally will run on port 5000

```
http://127.0.0.1:5000/ 
```

# Models

* **Movies** with attributes title and release date

* **Actors** with attributes name, age and gender

* **Shows** representing the many to many relationship of Movies and Actors

# Roles

## **Casting Assistant**
```
username: casting.assistant@email.com
password: adminADMIN12!
```
### Permissions:
* get:actors
* get:movies

## **Casting Director**
```
username: casting.director@email.com
password: adminADMIN12!
```
### Permissions:
* get:actors
* get:movies
* patch:actors
* patch:movies
* post:actors
* delete:actors

## **Executive Producer**
```
username: executive.producer@email.com
password: adminADMIN12!
```
### Permissions:
* get:actors
* get:movies
* patch:actors
* patch:movies
* post:actors
* post:movies
* delete:actors
* delete:movies

# Tokens

Test log in information here:
```
https://dev-yl9akfdv.us.auth0.com/authorize?
  audience=casting&
  response_type=token&
  client_id=h1BDlbmofIu7EMYKcTEbtCn6Xgsbeirj&
  redirect_uri=https://nano-proj5.herokuapp.com/
```
* Acquire tokens from **setup.sh** file

# Endpoints
* **GET** /actors and /movies
```
{
    "actors": [
        {
            "age": 34,
            "gender": "male",
            "id": 1,
            "name": "Alan Turing"
        },
        {
            "age": 52,
            "gender": "male",
            "id": 2,
            "name": "Linus Torvalds"
        },
        {
            "age": 28,
            "gender": "Female",
            "id": 3,
            "name": "Ada Lovelace"
        },
        {
            "age": 21,
            "gender": "Female",
            "id": 4,
            "name": "Grace Hopper"
        },

    ],
    "success": true
}
```

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Sat, 01 Jan 1994 00:00:00 GMT",
            "title": "Gladiator"
        },
        {
            "id": 2,
            "release_date": "Thu, 05 May 2005 00:00:00 GMT",
            "title": "The Dark Knight"
        },
        {
            "id": 3,
            "release_date": "Wed, 02 Feb 2022 00:00:00 GMT",
            "title": "Moana"
        },
        {
            "id": 4,
            "release_date": "Fri, 12 Apr 2002 00:00:00 GMT",
            "title": "Forrest Gump"
        },
    ],
    "success": true
}
```
* **DELETE** /actors/ and /movies/
```
{
    "delete": 1,
    "success": true
}
```

* **PATCH** /actors and /movies and
```
{
    "success": true,
    "updated": {
        "age": 22,
        "gender": "Female",
        "id": 1,
        "name": "Updated Actor"
    }
}
```

```
{
    "success": true,
    "updated": {
        "id": 1,
        "release_date": "Wed, 04 May 2005 23:00:00 GMT",
        "title": "The Gladiator!"
    }
}
```
* **POST** /actors/ and /movies/
```
{
    "actor": {
        "age": 28,
        "gender": "Male",
        "id": 1,
        "name": "New Actor"
    },
    "success": true
}
```

```
{
    "movie": {
        "id": 1,
        "release_date": "Sat, 06 Jun 2009 23:00:00 GMT",
        "title": "New Movie"
    },
    "success": true
}
```
# Tests

## Postman tests
* tested all endpoints authorisation

## test_app.py
* tested successful behaviour of each endpoint
* tested error behaviour of each endpoint
* tested RBAC for each role

You can set the database for testing locally in the setup.sh under:
```
export TEST_DATABASE_URL=<Enter you db url here>
```

# Dependencies

Dependencies and libraries used are listed in the requirements.txt as seen below:

```
alembic==1.6.5
click==8.0.1
ecdsa==0.17.0
Flask==1.1.2
Flask-Cors==3.0.10
Flask-Migrate==2.7.0
Flask-Script==2.0.6
Flask-SQLAlchemy==2.5.1
greenlet==1.1.0
gunicorn==20.1.0
itsdangerous==2.0.1
Jinja2==3.0.1
Mako==1.1.4
MarkupSafe==2.0.1
psycopg2-binary==2.9.1
pyasn1==0.4.8
python-dateutil==2.8.1
python-editor==1.0.4
python-jose==3.3.0
rsa==4.8
six==1.16.0
SQLAlchemy==1.4.18
Werkzeug==2.0.1
```

Python version is depicted in runtime.txt as seen below:
```
python-3.8.12
```

