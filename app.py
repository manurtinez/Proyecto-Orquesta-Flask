from flaskps import app
from flask import session
from flask_session import Session

if __name__ == '__main__':
    session.clear()
    app.run()