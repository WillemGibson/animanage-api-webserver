from init import db, ma

class User(db.model):
    __tablename__ = "Users"

    UserId = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.string, nullable=False, unique=True)
    Password = db.Column(db.string, nullable=False)
    IsAdmin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('UserId', 'Username', 'Password', 'IsAdmin')

user_schema = UserSchema(exclude=['password']) # {}
users_schema = UserSchema(many=True, exclude=['password']) # [{}, {}, {}]