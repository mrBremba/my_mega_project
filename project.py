from flask import Flask, render_template, request, redirect
from models import User, db_session, Base, engine


my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
    return render_template('index.html', title="Self Cultivation App (SCA)")

@my_flask_app.route('/registration/', methods=['POST'])
def registration():
    new_user = User(
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=request.form.get('password')
    )
    db_session.add(new_user)
    db_session.commit()
    return redirect("/", code=302)

@my_flask_app.route('/login/', methods=['POST'])
def login():
    #return render_template('login.html', email=request.form.get('email'),
    #password=request.form.get('password'))
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user = User.query.filter(User.email == user_email, User.password == user_password).first()
    if user:
        return redirect('/cabinet/')
    return redirect('/user_error/', code=302)

@my_flask_app.route('/user_error/')
def user_error():
    return render_template('user_error.html', title="Ошибка входа")
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user = User.query.filter(User.email == user_email, User.password == user_password).first()
    if user:
        return redirect('/cabinet/')
    return redirect('/user_error/', code=302)
    

@my_flask_app.route('/cabinet/')
def cabinet():
    return render_template('cabinet.html', title="Cabinet")

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    my_flask_app.run(debug=True, port=5005)