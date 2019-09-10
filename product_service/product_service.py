from flask import Flask, request, Response, url_for, render_template
from settings import *
import requests
from ProductModel import *

@app.route('/products', methods=['GET', 'POST'])
def products():
    token = request.args.get('token')
    resp = requests.get('http://localhost:5000/verifytoken?token='+token)
    if resp.status_code != 200:
        return Response('', 401, mimetype='application/json')

    if request.method == 'POST':
        request_data = request.get_json()
        name = str(request_data['name'])
        description = str(request_data['description'])
        price = float(request_data['price'])
        product = Product.add_product(name, description, price)
        return Response('', 201, mimetype='application/json')
    else:
        return render_template('products.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
