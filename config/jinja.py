# Jinja2 configuration file.

class JinjaConfig(object):
    # Returns the dictionary used to configure jinja2
    @staticmethod
    def getOptionsDict():
        return dict(trim_blocks = True, lstrip_blocks = True)
