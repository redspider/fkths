from trex.test import TestBase
from fkths import app
import fkths.model as m

class InitData(TestBase):
    """
    Initialise shared test data
    """

    critical_path = True
    order = 0

    def run(self):
        self.ok('init happened')
