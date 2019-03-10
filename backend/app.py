import logging.config
import os

# from backend.api.restplus import api
from flask import Flask, Blueprint
from backend.api.restplus import api
from backend.api.endpoints.users import ns as user_namespace

app = Flask(__name__, instance_relative_config=True)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure(application):
    # using main config.py configuration - currently not available
    application.config.from_object('config')

    # using instance configuration - from instance/ folder
    # application.config.from_pyfile('config.py')

    # configuration from enviromental variable - currently not available
    # (optional, chek start.sh in main directory)
    # app.config.from_envvar('APP_CONFIG_FILE')


def initialize(application):
    configure(application)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    application.register_blueprint(blueprint)


def main():
    initialize(app)
    log.info('>>> Starting server at http://{}/api/ <<<'.format(app.config['SERVER_NAME']))
    # log.warning('>>> Print server config <<<\n\n{}\n\n>>><<<'.format(app.config.items()))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
