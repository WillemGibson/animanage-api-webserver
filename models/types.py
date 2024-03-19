from init import db, ma

class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False, unique=True)

    reviews = db.relationship('Review', back_populates='Type')

class TypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type')

type_schema = TypeSchema() # {}
types_schema = TypeSchema(many=True) # [{}, {}, {}]

# {
#     id: 1,
#     status: Movie
# }