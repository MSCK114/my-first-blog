from pathlib import Path

# 构建项目内的路径，类似于：BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# 快速开始开发设置 - 不适用于生产
# 详细信息请参见：https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 安全警告：在生产中保持秘密的密钥！
SECRET_KEY = 'django-insecure-h$t%&qp2to$^wgunjnuzoift(rv6@)8ei5%)j6m-$t6sgqfd+='

# 安全警告：不要在生产中运行调试！
DEBUG = True

ALLOWED_HOSTS = []

# 应用程序定义

INSTALLED_APPS = [
    'django.contrib.admin',  # Django管理后台
    'django.contrib.auth',  # 用户认证
    'django.contrib.contenttypes',  # 内容类型
    'django.contrib.sessions',  # 会话管理
    'django.contrib.messages',  # 消息传递
    'django.contrib.staticfiles',  # 静态文件
    'forum',  # 您的论坛应用程序
    'userapp',  # 您的用户个人应用程序
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根URL配置
ROOT_URLCONF = 'djangoProject.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 模板目录
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

# WSGI应用程序
WSGI_APPLICATION = 'djangoProject.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'forum',                         # 数据库名称
        'USER': 'root',                         # 数据库用户名
        'PASSWORD': 'lxh123456',                # 数据库密码
        'HOST': '127.0.0.1',                    # 数据库主机
        'PORT': '3306',                         # 数据库端口
    }
}

# 密码验证
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
LANGUAGE_CODE = 'en-us'  # 指定网站使用的默认语言代码，'en-us'代表英语（美国）

TIME_ZONE = 'Asia/Shanghai'  # 指定网站使用的默认时区，'Asia/Shanghai'代表亚洲/上海时区，适用于中国上海地区

USE_I18N = True  # 启用国际化（Internationalization），允许网站支持多种语言

USE_TZ = True  # 启用时区支持，使得网站能够在不同时区正确显示时间和日期


# 静态文件（CSS、JavaScript、图片）
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'forum' / 'static'

# 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
