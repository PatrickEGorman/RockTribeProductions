from flask.ext.login import LoginManager
from app import app
from app.users.models import User

login_manager = LoginManager()
login_manager.init_app(app)
