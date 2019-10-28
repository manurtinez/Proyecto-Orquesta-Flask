from flask import render_template, abort, url_for, request, redirect, session, flash
from flaskps.models.usuario import User
from datetime import date

def registrar():
    if session['username'] != None:
        return render_template('user/registro.html')

def crear():
    if session['username'] != None:
        #User.create() esto falta
        return redirect(url_for('index'))
    else:
        p = request.form
        user = User.get_by_email(p['email'])
        if user:
            flash('el mail ya se encuentra registrado!')
            return redirect(url_for('registro'))
        else:
            User.create(p['email'], p['user'], p['password'], 1, date.today(), date.today(), p['nombre'], p['apellido'])
            session['username'] = p['user']
            return redirect('index')