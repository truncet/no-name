import os

DATABASE_URL = 'postgres://%s:%s@%s:%s/%s'%(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('POSTGRES_SERVICE_HOST'), os.environ.get('POSTGRES_SERVICE_PORT'), os.environ.get('DB_NAME'))
