class Config:
    """
    Still need to work on properly choosing each of subconfigs:
    DevelopmentConfig
    ProductionConfig
    """
    DEBUG = True
    TESTING = False
    ENV = 'default'
    SERVER_NAME = 'localhost:5000'

    UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False


class DevelopmentConfig(Config):
    ENV = 'developmentConfig'


class ProductionCOnfig(Config):
    DEBUG = False
    ENV = 'productionConfig'
