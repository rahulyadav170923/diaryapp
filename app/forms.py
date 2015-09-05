from flask_wtf import Form
from wtforms.fields import StringField, PasswordField,BooleanField
from wtforms.validators import Email,InputRequired,Length

class LoginForm(Form):
    email = StringField('email', [Email('incorrect email address')])
    password = PasswordField('Password', [InputRequired('enter password')])
    remember_me=BooleanField('remember_me',default=False)


class RegisterUser(Form):
	username = StringField('username', [InputRequired('enter name'),Length(max=20)])
	email = StringField('email', [Email('incorrect email address')])
	password = PasswordField('Password', [InputRequired('enter password')])
