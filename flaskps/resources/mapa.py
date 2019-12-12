from flask import redirect, url_for, render_template, session

def showMapa():
    return render_template(
        "verMapa.html",
    )

