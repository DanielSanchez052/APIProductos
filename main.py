import config
from flask import Flask,request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

mongo =  PyMongo(app)

@app.route('/product', methods=['POST'])
def add_products():
    try:
        if 'ref' in request.json and 'name' in request.json and 'coste' in request.json and 'stock' in request.json and 'available' in request.json:
            ref = request.json['ref']
            name = request.json['name']
            coste = request.json['coste']
            stock = request.json['stock']
            available = request.json['available']
            id = mongo.db.product.insert_one({
                "ref":ref,
                "name":name,
                "coste":coste,
                "stock":stock,
                "available":available,
            })
            return jsonify({'success':True}),201
        return jsonify({'success':False}),400
    except Exception as e:
        print(e)
        return jsonify({'success':False}),400

@app.route('/product', methods=['GET'])
def get_product():
    try:
        products = mongo.db.product.find()
        res = json_util.dumps(products)
        return Response(res, mimetype='application/json',status=200)
    except:
        return jsonify({'Not found':False}),404

@app.route('/product/<id>', methods=['GET'])
def get_product_by_id(id):
    product = mongo.db.product.find_one_or_404({'_id':ObjectId(id)})
    res = json_util.dumps(product)
    return Response(res, mimetype='application/json',status=200)

    
@app.route('/product/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    try:
        product = mongo.db.product.delete_one({'_id':ObjectId(id)})
        return jsonify({'success':True}),200
    except Exception as e:
        print(e)
        return jsonify({'success':False}),404

@app.route('/product/<id>', methods=['PUT'])
def update_product_by_id(id):
    # try:
        if 'ref' in request.json and 'name' in request.json and 'coste' in request.json and 'stock' in request.json and 'available' in request.json:
            ref = request.json['ref']
            name = request.json['name']
            coste = request.json['coste']
            stock = request.json['stock']
            available = request.json['available']

            book = mongo.db.product.update_one({'_id':ObjectId(id)},{"$set":{
                "ref":ref,
                "name":name,
                "coste":coste,
                "stock":stock,
                "available":available,
            }})
            print(book)
            # res = json_util.dumps(book)
            return jsonify({'success':True}),200#Response(res, mimetype='application/json',status=200)
        return jsonify({'Error al actualizar':False}),400

    # except:
    #     return jsonify({'success':False}),404

    
if __name__ == "__main__":
    app.run(port = 4500, debug=True)

