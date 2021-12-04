class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    MONGO_URI = "mongodb://localhost:27017/dbProducts"
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    UPLOAD_FOLDER = 'static/images/'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    FLASK_SECRET = SECRET_KEY

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_HOST = 'my.production.database' # not a docker link