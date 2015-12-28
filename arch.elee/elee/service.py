# -*- coding: utf-8 -*-

import logging
from zeus_core.service import Service
from . import thrift_file

service = Service(
    name='arch.elee',
    slug='elee',
    timeout=3 * 1000,

    thrift=thrift_file,
    service_name='ArgsService',

    user_exc=thrift_file.ArgsUserException,
    system_exc=thrift_file.ArgsSystemException,
    unknown_exc=thrift_file.ArgsUnknownException,
    error_code=thrift_file.ArgsErrorCode,
)

from dispatcher import *  # noqa Register dispatcher in this.