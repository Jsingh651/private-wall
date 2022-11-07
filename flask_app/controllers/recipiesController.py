from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.users import User
from flask_app.models.messages import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def newuser():
    return render_template('users.html')


@app.route('/register/user', methods = ['POST'])
def register ():
    if not User.validate(request.form):
        session['first_name'] = request.form['first_name']
        return redirect('/')  # back to login page
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    id = User.register(data)
    session['user_id'] = id
    return redirect('/dashboard')


# Login User route with post method form, lets users login #
@app.route('/login/user', methods = ['POST'])
def login ():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect ('/dashboard')


@app.route('/dashboard')
def dashboard():
    data = {'id': session['user_id']}
    users = User.get_all()
    message = Message.get_messages_with_user()
    message_len = Message.message_length(data)
    total_length = len(message) - len(message_len)
    reciver_len = Message.message_length_rec(data)
    rec_len = len(message) - len(reciver_len)
    return render_template('dashboard.html', loggedinuser = User.get_one(data),users = users,message = message,total_length = total_length,rec_len = rec_len )

@app.route('/create/post', methods = ['POST'])
def create_post():
    data = {
        'reciver_id':request.form['reciver_id'],
        'sender_id': request.form['sender_id'],
        'content': request.form['content']
    }
    Message.create_message(data)
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/delete/<int:id>')
def delete_message(id):
    data = {
        'id':id
    }
    Message.delete_message(data)
    return redirect('/dashboard')