from dotenv import dotenv_values

env = dotenv_values('.env')

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = env["SECRET_KEY"]
    DEBUG = True if env["DEBUG"] == "True" else False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env["DEV_DATABASE_URL"]

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env["TEST_DATABASE_URL"]

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env["DATABASE_URL"]

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}