import os

from celery import Celery

# 设置默认的Django配置模块，用于celery任务
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 初始化Celery应用
app = Celery('config')

# 从Django配置中加载Celery配置
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现Django项目中的任务模块
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

"""
定义一个Celery任务示例。
这个任务主要用于演示和调试，它打印当前任务的请求信息。
绑定到当前任务实例，忽略任务执行结果。
"""


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    # 打印任务请求的信息
    print(f'Request: {self.request!r}')
