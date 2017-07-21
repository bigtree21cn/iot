from marshmallow import fields, Schema, post_load
from .models import User


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password_hash = fields.Str()
    create_time = fields.DateTime()
    enabled = fields.Boolean()

    class Meta:
        exclude = ("id", "password_hash", "enabled")

    @post_load
    def make_users(self, data):
        return User(**data)