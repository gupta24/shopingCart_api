# shopingCart_api

## About the Rest_api

** first of all you will create the mongodb local server to run the api code..
* change database access password of local mongodb server in mongo_password.py file of Rest_Api project.


*** Second check for python3 and pip3 --version , if python3 and pip3 is not install then install .

*** Then open the linux terminal and go to the Rest_Api directory .
** Run the command..
- $ source venv/bin/activate
- $ flask run

** If flask is not run or any error then install (flask , flask-mongoengine ,    mongoengine , dnspython , httpie) by using the command..
- $ pip install flask
- $ pip install flask-mongoengine
- $ pip install mongoengine
- $ pip install dnspython
- $ pip install --upgrade httpie

 
** After flask run copy the local host is like  "http://127.0.0.1:5000/"
and run some command for use CURD operation on shoping cart api on other terminal..

# comment : this command run first to create a cart for the items .. 
- $ http POST http://127.0.0.1:5000/api/db_create_cart

# comment : this command run for get items in the cart ..
- $ http GET http://127.0.0.1:5000/api/getOrAddItem

# comment : this command run for add the item in cart ..
add_item_id_number - use any number like 4
add_item_name - use any like shoes
add_item_comapany_name - use any like nike
add_item_price - use any like Rs. 500

- $ echo '{"item_id":"add_item_id_number" , "item_name":"add_item_name", "item_company_name":"add_comapany_name", "item_price":"add_item_price"}' |http POST http://127.0.0.1:5000/api/getOrAddItem

# comment : this command run for delete the particular item from cart using item id number such that deleteItem/<item_id_number> ..
- $ http DELETE http://127.0.0.1:5000/api/deleteItem/2
 

# comment : this use for update the item by using item_id_number ..
- $ http PUT http://127.0.0.1:5000/api/deleteItem/3



                                 ***End***
