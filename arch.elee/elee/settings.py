# -*- coding: utf-8 -*-

# This is a very basic configuration file for elee.
# Uncomment or add what you need.

# ========== Huskar ==========
# from zeus_core.huskar import set_huskar_options
# set_huskar_options(local_mode=False)  # enable huskar in development


# ========== Cache Settings ==========
CACHE_NAMESPACE = "cache.elee" 
CACHE_SETTINGS = {
    "elee": "redis://localhost:6379"
}


# ========== DB Settings ==========
# Change the credentials in "master" and "slave" to your needs
DB_SETTINGS = {
    "elee": {
        "urls": {
            "master": "mysql+pymysql://root@localhost:3306/elee?charset=utf8",
            "slave": "mysql+pymysql://root@localhost:3306/elee?charset=utf8"
        },
        "max_overflow": -1,
        "pool_size": 10,
        "pool_recycle": 1200
    }
}


# ========== Async Settings ==========
# Enable async feature by uncomment following line, see
# also: `app.yaml`
# ASYNC_CELERYCONFIG = 'elee.celeryconfig'
ASYNC_ENABLED = False

from zeus_core.huskar import get_config_manager

config_manager = get_config_manager()

TEST_CONFIG = config_manager.get("TEST_CONFIG", "DEFAULT_VALUE")