# from flask_mail import Mail, Message
# from threading import Thread
#
# class Role(db.Model):
#     __tablename__='roles'
#     id=db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(64), unique=True)
#     users=db.relationship('User', backref='role', lazy='dynamic')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
# class User(db.Model):
#     __tablename__='users'
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(64), unique=True, index=True)
#     role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
# def send_email(to, subject, template, **kwargs):
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             # if app.config['FLASKY_ADMIN']:
#                 # send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'), known=session.get('known',False))
