import logging

from flask_restplus import Resource
from backend.api.restplus import api

from backend.db_substitute.models import User, USERS_LIST
from backend.api.serializers import user


log = logging.getLogger(__name__)
ns = api.namespace('users', description='Operations related to object type users')

parser = api.parser()
parser.add_argument('user', type=str, required=True, help='The user details', location='form')


def abort_if_user_not_exist(user_id):
    if user_id not in USERS_LIST:
        api.abort(404, "User {} does not exist".format(user_id))


@ns.route('/')
class UsersList(Resource):

    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list with users.
        """
        return [{'id': id, 'name': name} for id, name in USERS_LIST.items()]

    @api.response(201, 'User successfully created.')
    @api.expect(user)
    @api.doc(parser=parser)
    def post(self):
        """
        Creates a new user.
        """
        args = parser.parse_args()
        id = len(USERS_LIST)
        USERS_LIST[id] = args['user']
        return USERS_LIST[id], 201


@ns.route('/<int:id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class UserItem(Resource):

    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user.
        :param id: ID of a user
        """
        abort_if_user_not_exist(id)
        return USERS_LIST[id]

    @api.doc(parser=parser)
    @api.marshal_with(user)
    def put(self, id):
        """
        Update a user with provided ID
        :param id:
        """
        args = parser.parse_args()
        updated_user = args['user']
        USERS_LIST[id] = updated_user
        return updated_user, 204

    @api.doc(responses={204: 'User deleted'})
    def delete(self, id):
        """
        Delete a user with provided ID
        :param id:
        """
        abort_if_user_not_exist(id)
        del USERS_LIST[id]
        return None, 204
