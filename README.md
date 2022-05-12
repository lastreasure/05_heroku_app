# 05_heroku_app

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

https://nano-proj5.herokuapp.com/

## Set Up
 ``` 
 python3 -m venv venv
 source venv/bin/activate
 pip3 install -r requirements.txt
 python3 app.py 
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