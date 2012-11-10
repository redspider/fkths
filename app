#!/usr/bin/env python

from fkths.support.run import Manager
from fkths import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()