from functools import wraps
from urllib.parse import urlencode

from authlib.flask.client import OAuth
from flask import url_for, Blueprint
from flask import redirect
from flask import session

oauth = OAuth()

auth0_base_url = 'https://vgeorgescu.eu.auth0.com'

auth0 = oauth.register(
    'auth0',
    client_id='FPJFhuZhVWFDK5HHJd1nr2XFnBhD0Ddo',
    client_secret='E8TLg938z37ZxB5Ox_1SdqU6AVPL6d-O3JonmaaDXCxcwBKsYNMbm2WcPAJoGJIr',
    api_base_url=auth0_base_url,
    access_token_url=auth0_base_url + '/oauth/token',
    authorize_url=auth0_base_url + '/authorize',
    client_kwargs={
        'scope': 'openid profile',
    },
)

bp = Blueprint('auth', __name__)


# Callback that is called when the auth blueprint is registered on the app
def on_register(state):
    oauth.init_app(app=state.app)


bp.record_once(on_register)


# Here we're using the /callback route.
@bp.route('/callback')
def callback():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect(session.pop('url_to_return_to', url_for('main.home', _external=True)))


@bp.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=url_for('auth.callback', _external=True),
                                    audience=auth0_base_url + '/userinfo')


@bp.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('main.home', _external=True), 'client_id': 'FPJFhuZhVWFDK5HHJd1nr2XFnBhD0Ddo'}
    return redirect(auth0_base_url + '/v2/logout?' + urlencode(params))


# Decorator that redirects to login page when user is unauthenticated
def requires_auth(view_function):
    @wraps(view_function)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            session['url_to_return_to'] = url_for('main.' + view_function.__name__)
            return redirect('/login')
        return view_function(*args, **kwargs)

    return decorated
