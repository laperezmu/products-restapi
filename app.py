#Third party imports
from flask import Flask, jsonify, request

#Internal imports
from products import products

app = Flask(__name__)

#Index
@app.route('/', methods = ['GET'])
def ping():
    return jsonify({"message":"index"})


#View all products from products list
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)


#View one product with the name product_name from products list
@app.route('/products/<string:product_name>', methods = ['GET'])
def getProduct(product_name):
    for product in products:
        if product['name'] == product_name:
         return jsonify(product)
    return jsonify({"message": "Product not found"})



#Add a single product to products list
@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    for product in products:
        if product['name'] == new_product['name']:
            return jsonify({"message":"The product already exist"})
    products.append(new_product)
    return jsonify({"message":"Product added succesfully", "products": products})


#Update a single product with the name product_name from the products list
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    for product in products:
        if product['name'] == product_name:
            product['name'] = request.json['name']
            product['price'] = request.json['price']
            product['quantity'] = request.json['quantity']
            return jsonify({"message":"Product updated",
                            "product":product})
    return jsonify({"message": "Product not found"})


#Delete a single product with the name product_name from the products list
@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    for product in products:
        if product['name'] == product_name:
            products.remove(product)
            return jsonify({'message':'Product deleted',
                            "products": products})
    return jsonify({"message": "Product not found"})


if __name__ == '__main__':
    app.run(debug = True)

