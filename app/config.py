import os

try:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
except KeyError:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rocktribe:rocktribe@localhost:5432/rocktribe'


basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'rocktribe'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OPENID_PROVIDERS = [{"name": "test", "url": "test"}]