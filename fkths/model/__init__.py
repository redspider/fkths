from mongoengine import *
from datetime import datetime, timedelta
from mongoengine.queryset import DoesNotExist
from fkths import app

class User(Document):
    meta = {
        'indexes': [('email',)],
        }

    email      = EmailField(required=True)
    first_name = StringField()
    last_name  = StringField()
    time_zone  = FloatField()

    created    = DateTimeField(required=True, default=datetime.utcnow)
    last_login = DateTimeField()
    role       = StringField(required=True, default='user', choices=['user', 'admin'])

    def is_admin(self):
        return self.role == 'admin'

    def is_user(self):
        return self.role == 'user'

    def name(self):
        if not self.first_name is None and not self.last_name is None:
            name = "%s %s" % (self.first_name, self.last_name)
        elif not self.last_name is None:
            name = self.first_name
        else:
            name = ''
        return name
