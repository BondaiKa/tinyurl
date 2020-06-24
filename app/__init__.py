import redis
from config import Config
from flask import Flask

app = Flask(__name__)
redis = redis.Redis(host='redis', port=6379, decode_responses=True)

app.config.from_object(Config)

from app import routes
