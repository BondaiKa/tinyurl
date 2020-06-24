from app import routes
from flask import Flask
from config import Config
import redis


app = Flask(__name__)
redis = redis.Redis(host='redis', port=6379, decode_responses=True)

app.config.from_object(Config)
