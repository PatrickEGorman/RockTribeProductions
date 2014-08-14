# Flask config.py
import os

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgresql://rocktribe:rocktribe@localhost:5433/rocktribe"
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
DEBUG = True
