from flask import Flask , make_response , request , jsonify
from flask_mongoengine import MongoEngine
from mongo_password import password


app = Flask(__name__)

database_name = "shoping"
DB_URI = "mongodb+srv://rahul:{}@cluster0.w9xus.mongodb.net/{}?retryWrites=true&w=majority".format(password, database_name)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)


''' 
Sample Request Body
{
    "item_id": 1,
    "item_name": "t-shirt",
    "item_company_name": "puma",
    "item_price": "Rs. 200"
}
'''

class shoping_cart(db.Document):
    item_id = db.IntField()
    item_name = db.StringField()
    item_company_name = db.StringField()
    item_price = db.StringField()

    def to_json(self):
        # convert this document to JSON
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_company_name": self.item_company_name,
            "item_price": self.item_price
        }



@app.route('/api/db_create_cart', methods=['POST'])
def db_create_cart():
    item1 = shoping_cart(item_id=1, item_name="t-shirt", item_company_name="puma", item_price="Rs. 200")

    item2 = shoping_cart(item_id=2, item_name="pents", item_company_name="puma", item_price="Rs. 550")

    item1.save()
    item2.save()
    return make_response("", 201)




@app.route('/api/getOrAddItem', methods=['GET', 'POST'])
def getOrAddItem():
    if request.method == 'GET':
        items = []
        for item in shoping_cart.objects:
            items.append(item)
        return make_response(jsonify(items), 200)
    elif request.method == 'POST':
        content = request.json
        item = shoping_cart(item_id=content['item_id'], item_name=content['item_name'], item_company_name=content['item_company_name'], item_price=content['item_price'])

        item.save()
        return make_response("", 201)




@app.route('/api/deleteItem/<iId>', methods=['GET', 'PUT', 'DELETE'])
def deleteItem(iId):
    if request.method == 'GET':
        item_obj = shoping_cart.objects(item_id=iId).first()
        if item_obj:
            return make_response(jsonify(item_obj.to_json()), 200)
        else:
            return make_response("", 404)
    elif request.method == "PUT":
        # for update the item..

        content = request.json
        item_obj = shoping_cart.objects(item_id=iId).first()
        item_obj.update(item_name=content['item_name'], item_company_name=content['item_company_name'], item_price=content['item_price'])
        return make_response("", 404)
    elif request.method == "DELETE":
        #for dalete the any item..

        item_obj = shoping_cart.objects(item_id=iId).first()
        item_obj.delete()
        return make_response("", 204)




if __name__ == '__main__':
    app.run()

