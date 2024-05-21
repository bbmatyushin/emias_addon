import secrets


class AppConfig:
    DEBUG = True
    SECRET_KEY = secrets.token_hex()
