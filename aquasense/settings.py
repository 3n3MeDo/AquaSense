"""
Django settings for aquasense project.
Refactored for clarity and organization.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Load environment variables
load_dotenv()

# ==========================================
#              CORE SETTINGS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-=dq%4bkuawh7at@bl6l%!z8&+%)8lt7$bk@6)q@1_l2e9#z8%q'
DEBUG = True
ALLOWED_HOSTS = ['*']

# ==========================================
#           INSTALLED APPS
# ==========================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom Apps
    'reservations',
]

# ==========================================
#             MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'aquasense.middleware.AdminRedirectMiddleware',
]

ROOT_URLCONF = 'aquasense.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aquasense.wsgi.application'

# ==========================================
#              DATABASE
# ==========================================

import dj_database_url
import os # تأكد من استيراد os

# ... (باقي إعداداتك)

DATABASES = {
    'default': dj_database_url.config(
        # 1. القراءة من متغير البيئة 'DATABASE_URL' (الذي يوفره Railway)
        # 2. إذا لم يكن 'DATABASE_URL' موجودًا (أي تعمل محليًا)، يستخدم مسار SQLite المحلي.
        default=os.environ.get(
            'DATABASE_URL',
            'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
        ),
        conn_max_age=600
    )
}

# ... (باقي إعداداتك)
# ==========================================
#             AUTHENTICATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# ==========================================
#        STATIC FILES & STORAGE
# ==========================================

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================================
#        THIRD PARTY INTEGRATIONS
# ==========================================

# Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

# Resend Email API
RESEND_API_KEY = os.getenv('RESEND_API_KEY', 're_795aevhC_Gazmq9cbT9gidAW6n2SCvhRH')

# Security
CSRF_TRUSTED_ORIGINS = [
    'https://aquasense-production-c635.up.railway.app',
    'https://aquasense-production-c326.up.railway.app'
]

# ==========================================
#               LOGGING
# ==========================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'reservations': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
