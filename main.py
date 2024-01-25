from flask import Flask,jsonify
from extensions import db, jwt, admin
from auth import auth
from app import app_bp
from users import user_bp
from models import User,TokenBlocklist
from flask_cors import CORS
from flask_admin.contrib.sqla import ModelView


def create_app():             

    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = '11041a4a4adc392484b6eb4a'
    app.config['SECRET_KEY'] = 'skhbchrlhcgucuowxz'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize app 
    db.init_app(app)
    jwt.init_app(app)
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    
    CORS(app)
    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(user_bp)
    app.register_blueprint(app_bp)

    # load user
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_headers, jwt_data):
        identity = jwt_data["sub"]

        return User.query.filter_by(name=identity).one_or_none()

    # jwt error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({'message': "Token has expired", "error": "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'message': "Signature verification failed", "error": "invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'message': "Request does not contain a valid token", "error": "authorization required"}), 401

    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header,jwt_data):
        jti = jwt_data['jti']

        token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

        return token is not None

    return app