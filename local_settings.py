# -*- coding: utf-8 -*-

LOCAL_APP_CODE = "lj-jh-zxz-yty"
LOCAL_SECRET_KEY = '2T+*(0wFX)_gd2QAS$yNpEmaI~.T(F$IB-)Nlt4Dwq$(KJVkNz'


LOCAL_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 我们默认⽤用mysql
        'NAME': LOCAL_APP_CODE,
        'USER': 'root',
        'PASSWORD': "",
        'HOST': 'localhost',
        'PORT': 3306,
    },
}