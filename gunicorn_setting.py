# !/usr/bin/env python
# -*- coding: utf-8 -*

import multiprocessing, os

print('gunicorn config is running....')

bind = "0.0.0.0:8000"
#worker_class = "eventlet"
workers = 2
# workers = multiprocessing.cpu_count() * 2 + 1
pidfile = '/tmp/gunicorn.pid'
# accesslog = '/tmp/gunicorn_access.log'
errorlog = '/tmp/gunicorn_error.log'
loglevel = 'info'
capture_output = True
# statsd_host = 'localhost:8077'
proc_name = 'wind_blog'
daemon = True
# 测试确定，这里设置这个参数不生效
# django_settings = 'metamap.config.prod'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wind_blog.production")
