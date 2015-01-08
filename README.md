djember
=======

This is a skeleton app which wraps up an [Ember CLI](http://www.ember-cli.com/)(v0.13) frontend and a [Django](https://www.djangoproject.com/)(v1.7.1) backend. The Ember CLI app includes an token-based authentication controller, handled on the backend through [Django REST Framework](http://www.django-rest-framework.org/).

## Backend setup
* Environment
    * `mkvirtualenv backend`
    * `pip install -r requirements.txt`
* DB
    * `psql`
    * `User=# CREATE DATABASE backend;`
* settings
    * [Generate a new secret key](http://www.miniwebtool.com/django-secret-key-generator/)
    * `vi config/local.env`
    * Add `SECRET_KEY=<generated value>`
* Django
    * `./manage.py syncdb`
    * `./manage.py migrate`

## Frontend setup
* Environment
    * [Install the prerequisites](http://www.ember-cli.com/#getting-started)
* Dependencies
    * `bower install --save-dev bootstrap`

## Run
* Backend
    * `./manage.py runserver`
* Frontend
    * Built-in dev server
        * `ember server --proxy=http://127.0.0.1:8000/api`
    * Build and push to server
        * `ember build --environment=development`
