from app import app, views
from app.users import views
from app.users.admins import views

if __name__ == '__main__':
    app.run(debug=True)
