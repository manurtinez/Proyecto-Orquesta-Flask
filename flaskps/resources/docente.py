from flask import render_template, abort, url_for, request, redirect, session, flash
from flaskps.models import configuracion
from flaskps.models.usuario import User

def altaDocente():
    return render_template('/docente/altaDocente.html')