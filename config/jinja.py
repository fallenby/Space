# Jinja2 configuration file.

class JinjaConfig(object):
    @staticmethod
    def getOptionsDict():
        return dict(trim_blocks = True, lstrip_blocks = True)
