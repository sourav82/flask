from flask import Flask, request, Response, render_template, url_for
from settings import app
from UserModel import *
from functools import wraps
import jwt, datetime

@app.route('/login', methods=['GET', 'POST'])
def login():
    request_data = request.get_json()
    error = None
    if request.method == 'POST':
        username = str(request_data['username'])
        password = str(request_data['password'])
        match = User.is_valid(username, password)
        if match:
            expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
            token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
            return token
        else:
            return Response('', 401, mimetype='application/json')
    else:
        return render_template('login.html', error=error)

@app.route('/verifytoken')
def verify_token():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
        return Response('', 200, mimetype='application/json')
    except:
        return Response('Need a valid token to view this page', 401, mimetype='application/json')


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
