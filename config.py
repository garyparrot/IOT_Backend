import os

class Config:
    TEMPLATES_AUTO_RELOAD     = os.environ.get("TEMPLATES_AUTO_RELOAD").lower() == "true"
    SEND_FILE_MAX_AGE_DEFAULT = int(os.environ.get("SEND_FILE_MAX_AGE_DEFAULT"))
    DEBUG   = os.environ.get('DEBUG').lower() == "true"
    TESTING = os.environ.get('TESTING').lower() == "true"

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

class ProductionConfig(Config):
    DEBUG   = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

class ProductionConfig(Config):
    DEBUG   = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
