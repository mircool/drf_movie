"""
drf_movie项目的Django设置。

使用Django 5.0.6通过'django-admin startproject'生成。

有关此文件的更多信息，请参阅
https://docs.djangoproject.com/en/5.0/topics/settings/

有关设置的完整列表及其值，请参阅
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# 使用BASE_DIR构建项目内的路径，例如：BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent

# 快速启动开发设置 - 不适合生产
# 有关部署的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 安全性警告：在生产中使用时，请保持使用的密钥保密！
SECRET_KEY = 'django-insecure-q$=&&&7e)-*9$(94#+@y^n1c5%)3bkx+dww1jv*-^osomo#f^&'

# 安全性警告：不要在生产中开启调试模式！
DEBUG = True

ALLOWED_HOSTS = ['*']

# 应用定义

INSTALLED_APPS = [
    'django.contrib.admin',  # 管理员
    'django.contrib.auth',  # 认证
    'django.contrib.contenttypes',  # 内容类型
    'django.contrib.sessions',  # 会话
    'django.contrib.messages',  # 消息
    'django.contrib.staticfiles',  # 静态文件
    'rest_framework',  # REST框架
    'djoser',  # 用户认证
    'django_filters',  # 过滤器
    'movie',  # 电影应用
    'account',  # 用户应用
    'trade',  # 交易应用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # 国际化
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 数据库
# 有关数据库的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 密码验证
# 有关密码验证的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化
# 有关国际化的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# 静态文件（CSS、JavaScript、图像）
# 有关静态文件的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 媒体文件
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 默认主键字段类型
# 有关默认主键字段类型的更多信息，请参阅
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST框架设置
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# JWT设置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# DJOSER配置字典，用于配置Djoser库的行为。
DJOSER = {
    'USER_ID_FIELD': 'username',  # 用户ID字段
    'LOGIN_FIELD': 'email',  # 默认为'email'。
    'SEND_ACTIVATION_EMAIL': True,  # 是否发送激活邮件
    'ACTIVATION_URL': 'activate/{uid}/{token}',  # 激活链接
    'SEND_CONFIRMATION_EMAIL': True,  # 是否发送确认邮件
    'SERIALIZERS': {  # 序列化器
        'user_create': 'account.serializers.CustomUserCreateSerializer',  # 用户创建序列化器
        'current_user': 'account.serializers.CustomUserSerializer',  # 当前用户序列化器
    },
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,  # 是否显示未找到电子邮件
    'PASSWORD_RESET_CONFIRM_URL': 'password/{uid}/{token}',  # 重置密码确认链接
    'SET_PASSWORD_RETYPE': True,  # 是否重新输入密码
}

# 配置邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.vip.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'ynyjyz.kust@vip.163.com'
EMAIL_HOST_PASSWORD = 'QBLJMYIAQPZXGHPX'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# CSRF信任的源
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173', ]

# 支付宝支付配置
ALIPAY = {
    'app_id': '9021000137672118',
    'server_url': 'https://openapi-sandbox.dl.alipaydev.com/gateway.do',
    'app_private_key': 'MIIEowIBAAKCAQEAisKLoEO3Ui/ReWONWQNLFWbckCbjfUxvBcQhi75RR0iRLmKkJqXuKaCwR1GZcPID0ZDpOoglpMZA0Q9eYkX00qjFjQxWQ4XnqeoZIk9AJPQWqluuXTvnpqUa0UBpdsspT9t9UwLVxgyRJClqGBYfoCUkLwohc9pLXPPiHJvN9yaaYuGgb/XVCqnE47DXCDJhVKo1ZzfXG2Mj1ul2+t5Kjy92eVKvX2+OwEfkqDjdEr+LdRhNW2vvLF90KLf+WVpmQMO4Z8CPGbHO5qfAnNbeJvoSMgHN5Ft9ngy/pR+TaS4Ui7LSh0wMlHvQ7aa0BeTJuCZgKYVbd+KRQaQ9qGjH2wIDAQABAoIBAB+GLUR+veI9HODwHgev+Nnm4YsaWqp3t+1ebqSZ20tPkDQyksp4/g+VAxdg0XRYd0egHWx/y9WQeN9GF5JKBGHrl94AhISYolX26jjiOldq4M9ZPtbNqkYw0lPhx1QGud77pZA7X6e76SmHAyRvukWeyoapTYpNeLuoaKFJQFS6qY07WOqmK5vpQwKC4m1RMFhWXrmeHIIlc6oxAgEc8er+zxXz9D5QvkhP0SblIMYp9xrOi2PiRZJoTqdgiPf3/Qlewg3pWCdPv8BBNCnC3nhNgAc5ojQbB9u/BD4VritVLrNXhqgnBwVF4H6ZUuYvkghcXqfVb9yGtW71aZomqpECgYEAyyxhvXDruWvMBAvkkCBq+RhliXg0vAOeiV63WQRjWjI4fnbT/fK9Qk9V2CIvy7xIqkCPOyY2Qrr+E7lUtp0xgPoK5k7y0qztfAZe5LcoSF9huYKgthhdof8lIXYOtfqT5v4lQH2+/brgiQX/Fjr3FlwrapxcrWVaLSisQpm5VsMCgYEArtat/4nGjHIPpr8b/SyqEB/0bTXjYYO/Efkn2VKbJH7/A56mM4a2CV3o/zhvPVT5FaIiqS4dSOm0k7IQAROb0c59EIib1pUsmopMdmb2XZqvZdNw0WjUk3HOq3SvcKD5bnw8H3rY2IMbFk8741VQbJuKC+rLmPEUsaXS4kEKqQkCgYBfqF28W9YgTuiXXyIV2a2D6kCkILxzaSDTfIzGlJJSfSKsKDZXclo5RjEcubvXKKbtwceuCaeyc2f80V1ZPVl5aECJftJE7rZBlp5HARUuPfo85YvVMFOlWgOZZYQ3merY7v+LBalOvRXKbdBUHx8GoA6w+z2HRhjW+jdghBAHEQKBgHu144BA2IBf5Lsz1nYZuGuYcLclvjItqnDpP00Cqkv0oDTLeQZUd1HBZS/RmsRm76hjBOt4ebgxxVgMUk6wtTyLQusD/mCjROBEoz3UNNaesST3q4hBCMkbagTfl5O2E0geF9yea/knK29puRJuN23h0JgGFvGtA9t/XexB4W0hAoGBAKfn/sqdsQ1xV/JIqZ3uVY27LjunDJ7gfPvpE1/8KD2zNYHt/31y6dfyz7brFH0lBhUimWxI1aeCpmpDeRgXQvJBDdiT+tv9TYvuBOJG3stdxolI9wf0d0SMkkIV1tgIkNqY0GYF+f68OM9wi9A+sES0qv30rFsKPZxp2oA2ZGpY',
    'alipay_public_key': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgh8JVDRARcPCG2BThJE7AwFJMsSURowUlR7prwlhyIGKmagT/9+/GSRDggnRq9x8hh248MhDBpo/Iy9dcOVGXN3cT+ZPCKpGcfPR7UP6VE6l3yFxoP7EFKJbwtBfRQNT5YX0nGaojCW68Ue+uZqHnn76GJ4SvINnFMf0ptCMMubYA3m5SMzGneZLxp1KbOVeWARFoxeJ+94U/fKj0gSp3vbl4FbINes5mvv6L06f5HS6jBKcxG2qKjqBw28lse8zG+W1XIKT0YFfeuRboN3rlOQYaFO5oECsFVtZDxB6fj7C3l+L/Rrwu01iDyvRVCTienKGwAIvmAm6D5ZKJ9bzoQIDAQAB',
    'alipay_return_url': 'http://7883abc2.r21.cpolar.top/orders/',  # 支付成功后跳转的页面
    'alipay_notify_url': 'http://7883abc2.r21.cpolar.top/api/callback/',  # 支付成功后异步通知的地址
    'alipay_seller_id': '2088721036835160',  # 卖家ID
}
