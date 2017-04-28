from flask import render_template, session, redirect, url_for
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm
from datetime import datetime

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ..
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())


# from flask import render_template
# from . import main
#
#
# @main.route('/')
# def index():
#     return render_template('index.html')
