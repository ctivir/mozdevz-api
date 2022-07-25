# Mozdevz: Django API

This project is based on the React + Django Training by Mozdevz.  

## Table of contents

- [Mozdevz: React + Django Website](#mozdevz-react--django-website)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
    - [The challenge](#the-challenge)
    - [Links](#links)
  - [The process](#the-process)
    - [Built with](#built-with)
    - [How to contribute](#how-to-contribute)
    - [Useful resources](#useful-resources)
  - [Acknowledgments](#acknowledgments)

## Overview

### The challenge

- Build the website for the developer community based in Mozambique - [MozDevz Community](https://github.com/mozdevz)

### Links

[Mozdevz - Beta](https://mozdevz-api.herokuapp.com/api/) - Hosted at Heroku

[Figma Design](https://www.figma.com/file/aWCVAvMyCHSj0POFTU0w5Z/MozdevzUI?node-id=0%3A1) - Figma with the UI. Not done yet, contributors are welcome.

## The process

### Built with

- [Django](https://www.djangoproject.com/) - Python Web Framework
- [Django-Rest] Full documentation for the project is available at https://www.django-rest-framework.org/.

### Requirements

- Python (3.6, 3.7, 3.8, 3.9, 3.10)
- Django (2.2, 3.0, 3.1, 3.2, 4.0)

We highly recommend and only officially support the latest patch release of each Python and Django series.

### Installation

- Install using pip...

 1. pip install -r requirements.txt


### How to contribute

To contribute to this project you have to fork it and clone it.

After cloning it, in the project directory, run:

 
 1. `cd mozdevz-api` Get project folder
 2. `python3 -m venv env` create virtual env
 3. `ource env/bin/activate` activate virtual env
 4. `./python manage.py createsuperuser` create superuser to have access to django admin
 5. `./manage.py makemigrations` create new migrations based on the changes you have made to your models.
 6.  `./manage.py migrate` to appy all migrations.
 7.  `./manage.py runserver` to run the app in the development mode.
     Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

     The page will reload if you make edits.

### Useful resources

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)

## Acknowledgments

- [MozDevz Community](https://github.com/mozdevz)
- [Igor Sambo](https://twitter.com/LSambo02)
- [Cecilia Tivir](https://github.com/ctivir)
- [Olimpio Adolfo](https://twitter.com/rnrnshn)
