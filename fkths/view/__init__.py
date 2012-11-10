from fkths import app
from flask import request, g, session
import fkths.model as m
from fkths.view import index

@app.before_request
def check_auth(*args, **kwargs):
    if request.endpoint in ['static','cdn']:
        return

    g.user = None
    if 'user_id' in session:
        try:
            g.user = m.User.objects.get(id=session['user_id'])
        except m.DoesNotExist:
            del session['user_id']