from flask import render_template, flash, redirect
from app import app
from forms import LoginForm,RegisterUser

# index view function suppressed for brevity

@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('base.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('email requested ="%s",password="%s", remember_me=%s' %(form.email.data, form.password.data,str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In',form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        flash('username="%s",email requested ="%s",password="%s"' %(form.username.data,form.email.data,form.password.data))
        return redirect('/index')
    return render_template('register.html', title='RegisterUser',form=form)







