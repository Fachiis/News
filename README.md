****A Newspaper application****
-
> This is an application that uses Django to provide a platform where journalists can post articles, set up permissions so only the author of an article can edit or delete it, and finally add the ability for other users to write comments on each article.

## Features

- Django 3.2.10 & Python 3.7.12
- Install via [Pipenv](https://pypi.org/project/pip/)
- User sign up, log in/out, password reset
- Create an article by the authenticated user
- Edit an article by the authenticated user
- Delete an article by the authenticated user
- List all available articles
- Comment on an article by the authenticated user

The code style used for the project is PEP 8 -- Style Guide for Python Code and Flake8: For Style Guide
Enforcement.

---
## Table of Contents
* **[Installation](#installation)**
  * [Pipenv](#pip)
* [Setup](#setup)

---
## Installation
The application can be installed via Pipenv. To start,
clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Fachiis/News
$ cd News
```
```
$ python3 -m venv News
$ source News/bin/activate
(News) $ pipenv install --ignore-pipfile
(News) $ python manage.py migrate
(News) $ python manage.py createsuperuser
(News) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000/
```

## Setup

```
# Run Migrations
(News) $ python manage.py migrate

# Create a Superuser
(News) $ python manage.py createsuperuser

# Confirm everything is working:
(News) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000/
```