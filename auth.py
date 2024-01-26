from flask import Blueprint, jsonify,request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user,get_jwt, get_jwt_identity
from models import User,TokenBlocklist
from extensions import db, jwt

auth_bp = Blueprint('auth', __name__)

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

@auth_bp.post('/signup')
def signup():
    data = request.get_json()
    user = User.get_user_by_name(name= data.get('name'))

    if user is not None:
        return jsonify({"error": "User already exists"}), 403
    
    new_user = User(name=data.get('name'), email=data.get('email'))

    new_user.set_password(password=data.get('password'))

    new_user.save()

    return jsonify({"message": "User created"}), 201


@auth_bp.route('/login',  methods=["POST"])
def login():
    data = request.get_json()

    user = User.get_user_by_name(name=data.get("name"))

    if user and (user.check_password_hash(password=data.get("password"))):
        access_token = create_access_token(identity=user.name)
        refresh_token = create_refresh_token(identity=user.name)

        return (
            jsonify(token=str(access_token)),
            200,
        )

    return jsonify({"error": "Invalid name or password"}), 400

@auth_bp.get("/whoami")
@jwt_required()
def whoami():
    claims = get_jwt()
    return jsonify(
        {
            "message": "message",
            "user_details": {
                "name": current_user.name,
                "email": current_user.email,
            },
        }
    )

# regain access route 
@auth_bp.get("/refresh")
@jwt_required(refresh=True)
def refresh_access():
    identity = get_jwt_identity()

    new_access_token = create_access_token(identity=identity)

    return jsonify({"access_token": new_access_token})

@auth_bp.get('/logout')
@jwt_required(verify_type=False) 
def logout_user():
    jwt = get_jwt()

    jti = jwt['jti']
    token_type = jwt['type']

    token_b = TokenBlocklist(jti=jti)

    token_b.save()

    return jsonify({"message": f"{token_type} token revoked successfully"}) , 200