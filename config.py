import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevine:2001kevi@localhost/pitchapp'

class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True
    # enables debug mode
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
}