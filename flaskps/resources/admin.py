from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import usuario
from flaskps.db import get_db
from flaskps import app


