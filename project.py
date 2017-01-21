from flask import Flask, render_template, request, redirect
from models import User, db_session


my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
    return render_template('index.html', title="Self Cultivation")

@my_flask_app.route('/registration/', methods=['POST'])
def registration():
    new_user = User(request.form.get('name'), request.form.get('email'),
                    request.form.get('password'))
    db_session.add(new_user)
    db_session.commit()
    return redirect("/", code=302)

@my_flask_app.route('/login/', methods=['POST'])
def login():
    return render_template('login.html', email=request.form.get('email'),
                           password=request.form.get('password'))


if __name__ == '__main__':
    my_flask_app.run(debug=True, port=5005)
    