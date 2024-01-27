from extensions import db
# from faker import Faker
from app import app
from models import User, Product, Order, Cart, Address, Transaction

# fake = Faker()

# app = create_app()
# Create an application context
# app.app_context().push()

products = [{
  "id": 1,
  "image_url": "https://unsplash.com/photos/gray-and-black-sony-portable-mini-television-HWhR6lbn5xU",
  "name": "Classic Television",
  "price": 23,
  "category_id": 1
}, {
  "id": 2,
  "image_url": "https://unsplash.com/photos/selective-focus-photography-of-woman-holding-camera-gimbal-UqlWfdDiEIM",
  "name": "Sony Camera",
  "price": 78,
  "category_id": 2
}, {
  "id": 3,
  "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ariete.net%2Fen%2Fproduct%2FAriete-blender-579&psig=AOvVaw2KzT2eJ5rHx050favSiCo5&ust=1706434104202000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCPCnu8ug_YMDFQAAAAAdAAAAABAD",
  "name": "Blender",
  "price": 61,
  "category_id": 3
}, {
  "id": 4,
  "image_url": "https://unsplash.com/photos/black-smartphone-displaying-11-00-83ypHTv6J2M",
  "name": "Iphone 15",
  "price": 76,
  "category_id": 2
}, {
  "id": 5,
  "image_url": "https://unsplash.com/photos/an-orange-radio-sitting-on-top-of-a-red-surface-0-Eahp52PLk",
  "name": "Vintage Television",
  "price": 8,
  "category_id": 1
}, {
  "id": 6,
  "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.philips.co.ke%2Fc-p%2FHR1456_70%2Fdaily-collection-hand-mixers&psig=AOvVaw023un0-g8qQlU5n1pjEAx1&ust=1706434184454000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCNiEhPCg_YMDFQAAAAAdAAAAABAD",
  "name": "Hand mixer",
  "price": 78,
  "category_id": 3
}, {
  "id": 7,
  "image_url": "https://unsplash.com/photos/flat-lay-photography-of-black-sony-dslr-camera-on-black-surface-IVaKksEZmZA",
  "name": "Canon Lens",
  "price": 54,
  "category_id": 1
}, {
  "id": 8,
  "image_url": "https://unsplash.com/photos/purple-rotary-telephone-k5o-cuu9E6g",
  "name": "Purple Phone",
  "price": 26,
  "category_id": 2
}, {
  "id": 9,
  "image_url": "https://unsplash.com/photos/two-pink-dynatemp-410-tanks-on-front-of-white-wall-rwjz0jBZPqs",
  "name": "Cooking gas",
  "price": 4,
  "category_id": 3
}, {
  "id": 10,
  "image_url": "https://unsplash.com/photos/white-microwave-oven-turned-off-WtxE9xb0vQU",
  "name": "Microwave",
  "price": 44,
  "category_id": 3
}]

with app.app_context():
    db.session.add_all([Product(**rp) for  rp in products])
    db.session.commit()
    


