from __future__ import absolute_import

import os

if 'VIRTUAL_ENV' not in os.environ:
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    activate_this = os.path.join(project_root, 'bin', 'activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))

from flask.ext import script
import imp
import datetime

class Manager(script.Manager):
    def __init__(self, *args, **kwargs):

        super(Manager, self).__init__(*args, **kwargs)

        @self.command
        def runserver():
            "Run the development server"
            self.app.run()

        @self.shell
        def make_context():
            context = dict(
                app       = self.app,
                datetime  = datetime.datetime,
                timedelta = datetime.timedelta,
            )
            try:
                fp, path_name, description = imp.find_module('model', [self.app.root_path])
                context['m'] = imp.load_module('model', fp, path_name, description)
            except ImportError:
                pass

            return context

    def run(self, *args, **kwargs):
        if 'default_command' not in kwargs:
            kwargs['default_command'] = 'runserver'
        super(Manager, self).run(*args, **kwargs)