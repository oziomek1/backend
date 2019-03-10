from config.config import Config


class Production(Config):
    DEBUG = False
    ENV = 'production'
