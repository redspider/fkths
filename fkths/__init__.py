from trex.flask import Flask

class Fkths(Flask):
    def __init__(self, *args, **kwargs):
        super(Fkths, self).__init__(*args, **kwargs)

app = Fkths(__name__)

import trex.cdn
trex.cdn.FlaskCDN(app)

# Import these here to ensure that the app exists before all the code in the
# views/filters tries to execute
import fkths.view
import fkths.support.jinja_filters