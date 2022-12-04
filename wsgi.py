import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from app import app

api = app()

if __name__ == "__main__":
    api.run()