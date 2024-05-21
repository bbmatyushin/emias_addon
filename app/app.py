import datetime
from flask import Flask
from config import AppConfig


app = Flask(__name__)
app.config.from_object(AppConfig())
app.permanent_session_lifetime = datetime.timedelta(days=10)
