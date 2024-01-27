from extensions import db
# from faker import Faker
from app import app
from models import User, Product, Order, Cart, Address, Transaction, Category

# fake = Faker()

# app = create_app()
# Create an application context
# app.app_context().push()

products = [{
  "id": 1,
  "image_url": "http://dummyimage.com/209x100.png/dddddd/000000",
  "name": "Classic Television",
  "price": 23,
  "category_id": 1
}, {
  "id": 2,
  "image_url": "http://dummyimage.com/179x100.png/dddddd/000000",
  "name": "Sony Camera",
  "price": 78,
  "category_id": 2
}, {
  "id": 3,
  "image_url": "http://dummyimage.com/240x100.png/5fa2dd/ffffff",
  "name": "Blender",
  "price": 61,
  "category_id": 3
}, {
  "id": 4,
  "image_url": "http://dummyimage.com/201x100.png/ff4444/ffffff",
  "name": "Iphone 15",
  "price": 76,
  "category_id": 2
}, {
  "id": 5,
  "image_url": "http://dummyimage.com/106x100.png/cc0000/ffffff",
  "name": "Vintage Television",
  "price": 8,
  "category_id": 1
}, {
  "id": 6,
  "image_url": "http://dummyimage.com/215x100.png/5fa2dd/ffffff",
  "name": "Hand mixer",
  "price": 78,
  "category_id": 3
}, {
  "id": 7,
  "image_url": "http://dummyimage.com/173x100.png/ff4444/ffffff",
  "name": "Canon Lens",
  "price": 54,
  "category_id": 1
}, {
  "id": 8,
  "image_url": "http://dummyimage.com/111x100.png/ff4444/ffffff",
  "name": "Purple Phone",
  "price": 26,
  "category_id": 2
}, {
  "id": 9,
  "image_url": "http://dummyimage.com/120x100.png/ff4444/ffffff",
  "name": "Cooking gas",
  "price": 4,
  "category_id": 3
}, {
  "id": 10,
  "image_url": "http://dummyimage.com/161x100.png/cc0000/ffffff",
  "name": "Microwave",
  "price": 44,
  "category_id": 3
}]

categories = [{
  "id": 1,
  "name": "Entertainment"
}, {
  "id": 2,
  "name": "Communication"
}, {
  "id": 3,
  "name": "Kitchen Appliances"
}]

with app.app_context():
    db.session.add_all([Product(**rp) for  rp in products])
    db.session.commit()

    db.session.add_all([Category(**rp) for  rp in categories])
    db.session.commit()
    


