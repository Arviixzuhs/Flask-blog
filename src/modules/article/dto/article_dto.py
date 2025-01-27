from marshmallow import Schema, fields


class ArticleDTO(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str()
    tags = fields.Str()
