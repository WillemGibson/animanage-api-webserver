from datetime import timedelta 

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes

from init import db, bcrypt
from models.users import User, user_schema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/register", methods=["POST"]) # /auth/register
def auth_register():
    try:
        #  The data that we get in body of the request
        body_data = request.get_json()
        # create user insatnce
        user = User(
            username=body_data.get('username')
        )

        # password from the body request
        password = body_data.get('password')
        # if password exists, hash the password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8') 

        # add and commit the user to DB
        db.session.add(user)
        db.session.commit()
        # Respond back to the client
        return user_schema.dump(user), 201

    except IntegrityError as err:
        print(err.orig.pgcode)
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"Error": f"{err.orig.diag.column_name} is required"}
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"Error": "Username already in use"}, 409

@auth_bp.route("/login", methods=["POST"]) # /auth/login
def auth_login():
    # get data from request body
    body_data = request.get_json()
    # find user with particular username
    stmt = db.select(User).filter_by(username=body_data.get("username"))
    user = db.session.scalar(stmt)
    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create JWT token
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # return the token along with the user information
        return {"username": user.username, "token": token, "is_admin": user.is_admin}
    # else
    else:
        # return error
        return {"Error": "Invalid username or password"}, 401