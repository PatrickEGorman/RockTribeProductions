import os

DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'rocktribe'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']