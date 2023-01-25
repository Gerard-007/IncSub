from flask_restful import Resource, Api, marshal_with, fields


# Here i defined how the API should be displayed.
taskFields = {
    'id': fields.Integer,
    'name': fields.String,
    'status': fields.String,
    'last_updated': fields.DateTime
}