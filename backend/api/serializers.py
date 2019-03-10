from flask_restplus import fields
from backend.api.restplus import api


user = api.model('User', {
    'id': fields.Integer(readOnly=True, required=True, description='Unique user identifier'),
    'name': fields.String(required=True, description='User name'),
})
