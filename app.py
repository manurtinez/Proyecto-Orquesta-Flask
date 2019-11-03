from flaskps import app
from flask import session
from flask_session import Session

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    session.clear()
    app.run()