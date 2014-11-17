djember
=======

ember-cli + django

### Backend setup
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

### Frontend setup
* Environment
    * [Install the prerequisites](http://www.ember-cli.com/#getting-started)