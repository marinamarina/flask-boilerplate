from datetime import datetime
from flask import render_template, redirect, url_for, session, flash, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email
import os

__author__ = 'marinashchukina'


#route decorators
@main.route('/')
@main.route('/index')
def index():
    name = None
    return render_template('index.html', current_time=datetime.utcnow(), name=session.get('name'))

@main.route('/aboutMe', methods=['GET', 'POST'])
def aboutMe():
    form = NameForm()

    # is the form input valid?
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        # add a new user and send an email to the admin
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            print 'This is %r' % current_app.config['MAIL_PASSWORD']

            if current_app.config['FLASKY_ADMIN']:
                print 'meow'
                send_email(current_app.config['FLASKY_ADMIN'], 'New User','mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('aboutMe.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))
