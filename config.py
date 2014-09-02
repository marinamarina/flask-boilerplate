import os

__author__ = 'marinashchukina'

# absolute path to this script
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # encryption key, storing in an environment variable
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(23)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.environ.get('FLASKY_ADMIN')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = 'FLASKY'
    FLASKY_MAIL_SENDER='Flasky admin <flasky@admin.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# config dictionary
# mapping various configurations
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'deployment' : DeploymentConfig,

    'default' : DevelopmentConfig
}
