# -*- coding: utf-8 -*-
BROKER_URL = "amqp://ves:ves@172.16.10.83:5672/zeus"
CELERY_RESULT_BACKEND = 'redis://172.16.10.83:6379/0'
CELERY_DEFAULT_EXCHANGE = 'zeus'