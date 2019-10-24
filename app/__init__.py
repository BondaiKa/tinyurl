from flask import Flask
from config import Config
import redis

app = Flask(__name__)
redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

app.config.from_object(Config)

from app import routes