import logging

from flask_restplus import Api

log = logging.getLogger(__name__)


api = Api(
    version='1.0',
    title='Backend API',
    description='Backend API based on Flask'
)


@api.errorhandler
def default_error_handler(e):
    message = 'Unhandled exception occured'
    log.exception(message)

    # if not app.config['DEBUG']:
    if True:
        return {
            'message': message
        }, 500
