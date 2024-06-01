"""
drf_movie项目的Django设置。

使用Django 5.0.6通过'django-admin startproject'生成。

有关此文件的更多信息，请参阅
https://docs.djangoproject.com/en/5.0/topics/settings/

有关设置的完整列表及其值，请参阅
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

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

ALLOWED_HOSTS = []

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
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    'ACCESS_HEADER_TYPE': ('JWT',),
    'REFRESH_HEADER_TYPE': ('JWT',),
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
    },
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
