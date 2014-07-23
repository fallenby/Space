from config.jinja import JinjaConfig
from flask import Flask

# Overridden Flask object to allow for configuration of jinja2
class Flask(Flask):
    jinja_options = JinjaConfig.getOptionsDict()
