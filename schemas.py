from marshmallow import fields, Schema


class UserSchema(Schema): 
    id = fields.String()
    name = fields.String()
    email = fields.String()