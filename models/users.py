from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    reviews = db.relationship('Review', back_populates='user', cascade="")

class UserSchema(ma.Schema):
    reviews = fields.list(fields.Nested('ReviewSchema', exclude=['user']))

    class Meta:
        fields = ('id', 'username', 'password', 'is_admin')

user_schema = UserSchema(exclude=['password']) # {}
users_schema = UserSchema(many=True, exclude=['password']) # [{}, {}, {}]

# {
#   id: 1,
#   username: user1
#   reviews {
#       {id: 1, title: Anime 1}
#       {id: 2, title: Anime 2}
#       {id: 3, title: Anime 3}
# }