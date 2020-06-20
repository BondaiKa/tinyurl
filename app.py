import os

from app import app

HOST = os.environ.get('HOST')

if __name__ == "__main__":
    app.run(host=HOST, debug=False)
