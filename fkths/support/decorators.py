from decorator import decorator
from flask import url_for, g, request, redirect

def require_login(template=None):
    def decorated(f, *args, **kwargs):
        if not g.user:
            return redirect(url_for('auth.login', return_to = request.url))
        return f(*args, **kwargs)

    return decorator(decorated)