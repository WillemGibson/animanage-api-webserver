from init import db, ma
from marshmallow import fields

class ReviewsGenres(db.Model):
    __tablename__ = "reviews_genres"

    id = db.Column(db.Integer, primary_key=True)
    reviews_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class ReviewsGenresSchema(ma.Schema):
    review = fields.Nested('ReviewSchema')
    genre = fields.Nested('GenreSchema')

    class Meta:
        fields = ('id', 'review_id', 'genre_id')

# # {
# #     review_id: 1,
# #     genre_id: 3
# # }