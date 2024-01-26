from flask import Flask,jsonify
from extensions import db, jwt, admin
from auth import auth_bp
from main import main_bp
from users import user_bp
from models import User
from flask_cors import CORS
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate


def create_app():             

    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = '11041a4a4adc392484b6eb4a'
    app.config['SECRET_KEY'] = 'skhbchrlhcgucuowxz'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize app 
    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    
    CORS(app)
    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)

    

    return app

app = create_app()