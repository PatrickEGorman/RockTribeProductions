from app import app, views
from app import config
from app.config import secret_key
from app.users import views
from app.users.admins import views
from app.users.comments import views

if __name__ == '__main__':
    app.run(debug=True)
