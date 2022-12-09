# TAMU FOODS
---
This is an e-Commerce food delivery web-based application that enables users to order food online from our partner range of restaurants and individual vendors.

A sequel and beta version of [Tamu-Foods](https://github.com/John-Kimani/Tamu-Foods-BackEnd.git) that I had earlier made with the Flask framework and alpha version of [TamuFoods](https://github.com/John-Kimani/tamufoods_react_redux_express.git) I recently revamped using React, Redux and Node express.

![Tamu Foods Homepage](static/assets/homepage.png)

## Table of contents
1. [Overview](#project-overview)
2. [Features](#features)
3. [Demo](demo)
4. [Setup](#setup)
5. [Author](#author)

## Overview
---
TamuFoods is a kenyan Food Tech company that seek to facilitate trade between vendors, merchants and customers through an e-Commerce platform.
Unlike the existing food deliver applications that focuses on established restaurants, we seek to expand our vendors base by allowing private chefs, catering students, and other professionals who love cooking join the platform to sell their recipes.

## About Project
---

The application is built into two broad categories:
- Hompage
    - [x] General information about the company.
    - [x] Imporant links to contact administration.
    - [ ] Provision to press and publications.
    <br>
- Menupage
    - [x] View product catalogue.
    - [x] Process product purchase(add to cart)

- Cart
    - [x] View selected customer items.
    - [x] Adjust invenory.
    - [x] Initiate checkout process.
    - [x] Save and clear cart items.

### Users
<hr>
This platform offers multi user roles.

#### Customers
- [x] Self register.
- [x] View client oriented view ports and other allowed permisions.
- [x] Initiate and process orders.
- [x] Request on location delivery.
- [x] Customize personal profile and information.

#### Business Admin
Defined as a sole proprietor, business owner or a registered company patnering with Tamu Foods.

**Vendor** - Legal partner to TamuFoods offering food items.
**Merchant** - Possible potential 3rd party trade facilitators. 
They include, delivery company or individuals, suppliers, government, financial and non-financial instiutions etc.

- General responsibilities.
    - [x] Registered as a vendor in application.
    - [x] Customize personal profile and account information.
    - [x] Status
        - On registration and incase of suspension = Pending.
        - Upon verification = Approved.
        - Incase of withdrawal = Rejected.
    - Approved vendors can:
        - [x] Create food items and assign food category they deal in.
        - [x] Manage their inventory.
        - [x] View sales reports and business accounts.
    - Approved merchants e.g delivery C/O can:
        - [x] Process delivery.
        - [x] View delivery reports. 
#### System Admin
- System admin has superuser prvilideges to maintain the application.
    - [x] Manages all users, inventory and has access to all the available models.
    - [x] Verifies and approves users registered as Merchants and vendors.

## Features
---
1. MultiUser Roles, permission and authentication
2. Custom profile interface. i.e user can update personal information
3. e-Commerce shopping experience.

## Technologies used
---

<table>
    <tr>
        <th>Development</th>
        <td>Django 4.1.3 </td>
        <td>Postgress</td>
    </tr>
    <tr>
        <th>Production</th>
        <td>Hosted on Railway</td>
        <td> <a href="https://tamufoods-by-kimperria.up.railway.app/">LiveLink</a> </td>
    </tr>
</table>

### Project illustations

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