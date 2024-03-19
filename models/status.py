from init import db, ma
from marshmallow import fields

class Status(db.Model):
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False, unique=True)

    reviews = db.relationship('Review', back_populates='Status')

class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'status')

status_schema = StatusSchema() # {}
statuss_schema = StatusSchema(many=True) # [{}, {}, {}]

# {
#     id: 1,
#     status: In progress
# }