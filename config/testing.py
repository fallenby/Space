# Testing environment configuration object for Flask.

from config.base import Config

class Config(Config):
    TESTING = True
