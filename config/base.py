# Base object for configuration object for Flask.
# This object is overridden in other files to specify varying configuration options.

class Config(object):
    DEBUG = False
    TESTING = False
    DATABSE_URI = ''
