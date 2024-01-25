from flask import Blueprint, jsonify,request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, current_user,get_jwt, get_jwt_identity
from models import User,TokenBlocklist

auth = Blueprint('auth', __name__)

@auth.post('/signup')
def signup():
    data = request.get_json()
    user = User.get_user_by_name(name= data.get('name'))

    if user is not None:
        return jsonify({"error": "User already exists"}), 403
    
    new_user = User(name=data.get('name'), email=data.get('email'))

    new_user.set_password(password=data.get('password'))

    new_user.save()

    return jsonify({"message": "User created"}), 201


@auth.route('/login',  methods=["POST"])
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

@auth.get("/whoami")
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
@auth.get("/refresh")
@jwt_required(refresh=True)
def refresh_access():
    identity = get_jwt_identity()

    new_access_token = create_access_token(identity=identity)

    return jsonify({"access_token": new_access_token})

@auth.get('/logout')
@jwt_required(verify_type=False) 
def logout_user():
    jwt = get_jwt()

    jti = jwt['jti']
    token_type = jwt['type']

    token_b = TokenBlocklist(jti=jti)

    token_b.save()

    return jsonify({"message": f"{token_type} token revoked successfully"}) , 200