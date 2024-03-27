import os
from dotenv import load_dotenv

# Load environment variables from .env file
current_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(current_dir, '.env')
load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.getenv("DATABASE_HOST"))
    DATABASE = str(os.getenv("DATABASE_NAME"))
    USERNAME = str(os.getenv("DATABASE_USERNAME"))
    PASSWORD = str(os.getenv("DATABASE_PASSWORD"))
    PORT = str(os.getenv("DATABASE_PORT")) if os.getenv("DATABASE_PORT") else '3306'

    JWT_SECRET_KEY = str(os.getenv("JWT_SECRET_KEY"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':'+ PORT +'/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
