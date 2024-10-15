import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  APPLICATION_ROOT='/api/v1'
  ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
  UPLOAD_FOLDER='/static'
  TESTING = False
  SECRET_KEY = os.getenv('SECRET_KEY')
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
  TIMEZONE = timedelta(days=1)
  SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
  GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
  GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')



class Production(Config):
  ENV = 'production'
  DEBUG = False

class Development(Config):
  ENV = 'development'
  DEBUG = True
  DEVELOPMENT = True
