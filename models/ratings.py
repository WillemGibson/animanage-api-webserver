from init import db, ma

class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False, unique=True)

    reviews = db.relationship('Review', back_populates='Rating')

class RatingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating')

rating_schema = RatingSchema() # {}
ratings_schema = RatingSchema(many=True) # [{}, {}, {}]

# {
#     id: 1,
#     status: 3
# }