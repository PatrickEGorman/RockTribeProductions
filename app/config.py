import os
from app import app
app.config["DEBUG"]=True
try:
    secret_key = os.environ['SECRET']
except KeyError:
    secret_key = "X_C@]s\xd2\xbf\xd1\xdc\x85\xc4\xb8\xf1\xb6\n\xfa\xd9\xb2\x1aQ0\x03\xc1"

try:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
except KeyError:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rocktribe:rocktribe@localhost:5432/rocktribe'


basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
CSRF_ENABLED = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
