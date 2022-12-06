# TAMU FOODS
---
This is an e-Commerce food delivery web-based application that enables users to order food online from our partner range of restaurants and individual vendors.

A sequel and beta version of [Tamu-Foods](https://github.com/John-Kimani/Tamu-Foods-BackEnd.git) that I had earlier made with the Flask framework.

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
Development
Framework
Database
## Features
---
1. MultiUser Roles, permission and authentication
2. Custom profile interface. i.e user can update personal information
3. e-Commerce shopping experience.

#### Customer Role

#### Vendor Role

#### Merchant Role
## Technologies used
---
### Project illustations
---

<table>
    <tr>
        <th>UI UX Prototype</th>
        <th>DATABASE</th>
    </tr>
    <tr>
        <td>Click link to view wireframe and design concept on <a href="https://www.figma.com/file/YpZpvOnzbIiJ9zGNQ7l1Ta/Tamu-Foods-with-Django?node-id=0%3A1">Figma</a></td>
        <td>Click link to view schema on <a href="https://miro.com/app/board/uXjVPHwAag8=/?share_link_id=965173040672">Miro </a> </td>
    </tr>

</table>

## Setup
### Dependacies
- Python 3.6 +
- PostgreSQL
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
###### Set and configure your development variables.
    - SECRET_KEY='django-secret-key' or 'you-will-never-guess'
    - MODE='dev'
    - DEBUG=True
    - DB_NAME='blackpanther22'
    - DB_USER='postgres user' or 'allowed psql user'
    - DB_PASSWORD='you-will-never-guess' or Null
    - DB_HOST=provide for all or default
    - ALLOWED_HOSTS=provide for localhost
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