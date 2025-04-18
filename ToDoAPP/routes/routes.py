from flask import render_template, request, redirect, url_for
from flask_login import current_user

from ToDoAPP import db
from ToDoAPP.routes import routes_bp
from ToDoAPP.models import User
from ToDoAPP.utils import send_email

# index route for front page
@routes_bp.route('/')
def index():
    return render_template('index.html')



@routes_bp.route('/faq')
def faq():
    return render_template('faq.html')


@routes_bp.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        body = request.form.get("message")
        send_email(email, name, body)
        return redirect(url_for('routes.contact'))
    if current_user.is_authenticated:
        result = db.session.execute(db.select(User).where(User.id == current_user.id))
        user = result.scalars().all()[0]

        return render_template('contact.html', user=user)
    else:
        return render_template('contact.html')


