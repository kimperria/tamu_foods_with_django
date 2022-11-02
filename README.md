# TAMU FOODS
---
This is an e-Commerce food delivery web-based application that enables users to order food online from our partner range of restaurants and individual vendors.
A sequel and beta version [Tamu-Foods-With-Flask](https://github.com/John-Kimani/Tamu-Foods-BackEnd.git) of that I had made with Flask.

## Table of contents
1. [Overview](#project-overview)
2. [Features](#features)
3. [Demo](demo)
4. [Setup](#setup)
5. [Author](#author)

## Project Overview
---

## About Project
---
## Features
---
## Technologies used
---
### Project illustations
---
Database schema flow chart click here to view.
UI/UX prototype click here to view.
Project Management click here to view.

## Setup
### Dependacies
- Python 3.6 +
- IDE of choice.
- More listed on requirements.txt
#### How to install this project:
    - Clone this repo, run:
        git clone https://github.com/John-Kimani/tamu_foods_with_django.git
    - Move into the project folder:
        cd tamu_foods_with_django
    - Open project with IDE i.e VsCode run:
        code .
    - Create projects virtual environment and install all packages
      virtualenv venv
      pip install -r requirements.txt
    - Activate virtual environment
        pipenv shell
    - Create postgress DB
        sudo -u postgres psql
        password for user i.e: 'you-will-never-guess'
        postgres=#: CREATE DATABASE blackpanther22;
        CREATE DATABASE
    - Set your environment variables, keys and other configurations


### Environment variables
    - SECRET_KEY='you-will-never-guess'
    - MODE='dev'
    - DEBUG=True
    - DB_NAME='blackpanther22
    - DB_USER='user'
    - DB_PASSWORD=Null
    - DB_HOST=all
    - ALLOWED_HOSTS=all
    - CLOUDINARY_CLOUD_NAME='your cloudinary username'
    - CLOUDINARY_API_KEY='your cloudinary api'
    - CLOUDINARY_API_SECRET='your cloudinary secret key'

### Continue with setup
    - Make migrations and migrate configurations to new DB
        python manage.py makemigrations
        python manage.py migrate
    - Run entry file:
        python3 manage.py runserver
    - Create superuser
        python manage.py createsuperuser


## Author
---
This project was designed and developed by : [Kimani John](https://kimanijohn.netlify.app/)