from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import usuario
from flaskps.db import get_db

#administracion: conecta con la ruta area admin
@app.route('/administracion.html')
def administracion():
     return render_template('administracion.html')