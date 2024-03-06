from flask import Flask

app = Flask(__name__)

# must import routes after we define the application
from app import routes
