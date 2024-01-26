from extensions import db
from faker import Faker
from app import create_app
from models import User, Product, Order, Cart, Address, Transaction

fake = Faker()

app = create_app()
# Create an application context
app.app_context().push()

def generate_fake_data():
    # Generate fake data
    users = [User(name=fake.name(), email=fake.email()) for _ in range(10)]
    products = [
        Product(name=fake.word(), price=fake.random_number(2), image_url=fake.image_url()) for _ in range(10)
    ]
    carts = [Cart(user=user) for user in users]
    addresses = [
        Address(user=user, street=fake.street_address(), city=fake.city()) for user in users
    ]

    # Add data to the database session
    db.session.add_all(users + products + carts + addresses)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    generate_fake_data()
