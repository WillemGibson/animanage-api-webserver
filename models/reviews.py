from init import db, ma
from marshmallow import fields

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    # status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    # type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    # rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'), nullable=False)
    # genre
    eps_watched = db.Column(db.Integer, nullable=True)
    eps_total = db.Column(db.Integer, nullable=True)
    date_started = db.Column(db.Date, nullable=True)
    date_finished = db.Column(db.Date, nullable=True)
    recom =  db.Column(db.Boolean, default=False)
    fav = db.Column(db.Boolean, default=False)
    com = db.Column(db.String(2000), nullable=True) # String("Max length of an input")

    user = db.relationship('User', back_populates='reviews')
    # status = db.relationship('Status', back_populates='reviews')
    # type = db.relationship('Type', back_populates='reviews')
    # rating = db.relationship('Rating', back_populates='reviews')

class ReviewSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username'])
    # status = fields.Nested('StatusSchema', only=['status'])
    # type = fields.Nested('TypeSchema', only=['type'])
    # rating = fields.Nested('RatingSchema', only=['rating'])

    class meta:
        fields = ('id', 'user', 'title', 'status', 'type', 'rating', 'eps_watched', 'eps_total', 'date_started', 'date_finished', 'recom', 'fav', 'com')
    
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

# {
#     id: 1,
#     user: {username: user1},
#     title: Anime 1,
#     status: {status: Not Started},
#     type: {type: Series},
#     rating: {rating: 5},
#     eps_watched: 14,
#     eps_total: 25,
#     date_started: 14/03/2024,
#     date_finished: 19/03/2024,
#     recom: 0,
#     fav: 1,
#     com: "I enjoyed it! But never finished it"
# }