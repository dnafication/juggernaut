from celery import Celery
import os
import time

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('trycelery', broker='redis://localhost:6379', backend='redis://localhost:6379')

@app.task
def add(x, y):
    time.sleep(50)
    return x + y

# app.conf.broker_url = 'redis://localhost:6379/0'

# Run following
# celery -A trycelery worker --loglevel=info
