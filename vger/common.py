import json
import os
import glob
from jinja2 import Environment, FileSystemLoader


class core:
    def _read_template(self, template_name):
        loc = os.path.dirname(__file__)
        template_dir = os.path.abspath(os.path.join(loc, "_templates"))
        env = Environment(loader=FileSystemLoader(template_dir))
        return env.get_template(template_name)