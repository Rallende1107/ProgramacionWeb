from pathlib import Path

from prueba3.settings.base import BASE_DIR
# BASE_DIR = Path(__file__).resolve().parent.parent


SQLite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': BASE_DIR / 'rene.sqlite3',
    }
}

# pip install psycopg2
PostgreSQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '1107',
    }
}

# pip installl mysqlclient
MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# pip install cx_oracle
Oracle = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/xepdb1',
        'USER': 'Miusuario',
        'PASSWORD': '123',
        # 'TEST': {
        #     'USER': 'default_test',
        #     'TBLSPACE': 'default_test_tbls',
        #     'TBLSPACE_TMP': 'default_test_tbls_tmp',
        # },
    }
}