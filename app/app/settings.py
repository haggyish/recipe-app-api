"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@4g#*b7$oubes@r7@c=a58+71yfr_bfsf1ul386ku)d!gdr)b!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

        #next we can move on to our
        #settings.py and we can customize our user model in here.  So I like
        #to scroll to the bottom and add any new settings I add to the bottom
        #because it just is logical.  And we're gonna create a new setting
        #called AUTH_USER_MODEL and it needs to be all caps and what we do
        #is we assign a string here and we set the string to core.User so
        #core is the name of our app and user is the name of the model in
        #our app that we want to assign as the custom user model.

AUTH_USER_MODEL = 'core.User'


        #  okay so
        #make sure that we save that settings.py file and then let's head
        #back to our terminal and let's make our migrations.



        #kkSo we're gonna
        #type docker-compose run app sh -c python manage.py make migrations
        #and I like to specify the name of the app that we're going to make
        #the migrations for even though it's not always necessary I find
        #that sometimes it doesn't work just running make migrations on its
        #own sometimes you need to specify the app.
        #
        # docker-compose run app sh -c "python manage.py makemigrations core"

        # I'm not sure why that
        #is I think it may be a bug or something in Django Okay now let's
        #hit enter and what this is going to do it's going to run our database
        #migrations which will create a new migrations file here.  Which
        #basically it is the instructions for Django to create the model in
        #the real database that we use.  So we don't really need to worry
        #too much about this migration file it's kind of an advanced feature
        #if you want to mess around with this file.  But all you need to
        #know is that these migrations are always used to set up the database
        #and every time you make a change to the models you need to run the
        #migrations again.  Okay so now we have our migrations we can run
        #our tests again and hopefully they should pass.
        #
        # docker-compose run app sh -c "python manage.py test && flake8"
        #
        # Okay so you can
        #see that the test ran and it all came back okay.  So basically that
        #is our first core app test driven development feature that we're
        #going to commit into our app.  But before we're going to do that
        #we're going to make some more changes to it in some future videos.
