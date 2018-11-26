from flask import render_template, url_for, flash, redirect, request
from incidtracker import app, db, bcrypt
from incidtracker.forms import RegistrationForm, LoginForm
from incidtracker.models import User, Incident
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def home():
    incidents = Incident.query.all()
    return render_template('home.html', incidents=incidents)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('The account has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/incident", methods=['GET', 'POST'])
def incident():
    form = IncidentForm()
    if form.validate_on_submit():
        # time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        incident = Incident(category=form.category.data, 
                            description=form.description.data, 
                            state=form.state.data, 
                            poc=form.poc.data, 
                            tag=form.tag.data, 
                            assignee=form.assignee.data)
        db.session.add(incident)
        db.session.commit()
        flash('New incident added!', 'success')
        return redirect(url_for('home'))
    return render_template('incident.html', title='New Incident', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))