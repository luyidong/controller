from deis.settings import *  # noqa

# security keys and auth tokens
with open('/var/run/secrets/api/builder/auth/builder-key') as f:
    BUILDER_KEY = f.read().strip()

with open('/var/run/secrets/api/django/secret-key') as f:
    SECRET_KEY = f.read().strip()

with open('/var/run/secrets/deis/database/creds/user') as f:
    DATABASES['default']['USER'] = f.read().strip()

with open('/var/run/secrets/deis/database/creds/password') as f:
    DATABASES['default']['PASSWORD'] = f.read().strip()

DATABASES['default']['NAME'] = DATABASES['default']['USER']