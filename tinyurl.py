import os

from app import app
from config import Config

HOST = os.environ.get('HOST')

if __name__ == "__main__":
    app.run(host=HOST, debug=False)
