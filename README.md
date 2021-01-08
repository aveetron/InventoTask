# InventoTask

## please read the 'API Documentation' from the 'Api documentation' folder.

### in case of CORS errors for communicating with frontend frameworks like angular,vuejs,react,
### please install 'cors-headers'

## for installing cors-header - 'pip install django-cors-headers'

## then add this package to your installed app list, like :


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

## and then add this on django middleware for deliverng request and response properly.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


## after that add the frontend end point link into settings.py, like -

CORS_ORIGIN_WHITELIST = 'http://localhost:4200',
