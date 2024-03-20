from init import db, ma
from marshmallow import fields

class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=False, unique=True)
    
    reviews = db.relationship("Review", back_populates="genres", secondary='reviews_genres')

class GenreSchema(ma.Schema):
    reviews = fields.List(fields.Nested('ReviewSchema', dump_only=True))

    class Meta:
        fields = ('id', 'genre')

genre_schema = GenreSchema() # {}
genres_schema = GenreSchema(many=True) # [{}, {}, {}]

# {
#     id: 1,
#     status: 3
# }