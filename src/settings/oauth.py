from authlib.integrations.flask_client import OAuth


oauth = OAuth()

CONF_URL='https://accounts.google.com/.well-known/openid-configuration'

oauth.register(name='google',server_metadata_url=CONF_URL,client_kwargs={'scope':'openid email profile'})