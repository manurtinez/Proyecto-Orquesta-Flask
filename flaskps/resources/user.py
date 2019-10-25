from flask import render_template, abort, url_for, redirect, session
from flaskps.models.usuario import User

def registrar():
    if session['username'] != None:
        return render_template('user/registro.html')

def crear():
    if session['username'] != None:
        #User.create() esto falta
        return redirect(url_for('index'))