# -*- coding: utf-8 -*-

import logging
from .service import service
from .models import TodoList
from zeus_core.health import alternative
from zeus_core import signals
from thrift.Thrift import TException
from zeus_core.metrics import get, counters, incr
from .exc import raise_system_exc, ArgsSystemException
import time

logger = logging.getLogger(__name__)


@service.dispatcher
class Dispatcher(object):
    def __init__(self):
        logger.info('arch.elee server starting..')

    def ping(self):
        return True

    def yay(self, id):
        return True

    def nay(self, id):
        return False

    def add_todo(self, title):
        TodoList.add(title)

    def list_todo(self):
        return TodoList.list()

    def complete_todo(self, _id):
        TodoList.complete(_id)

    def counters_init(self):
        counters.clear()
        incr('arch.elee.even')
        incr('arch.elee.even.sys_exc')
        counters['arch.elee.even'].clear()
        counters['arch.elee.even.sys_exc'].clear()
        counters['arch.elee.even']._clock = time.time()
        counters['arch.elee.even.sys_exc']._clock = time.time()
        incr('arch.elee.even', 19)
        incr('arch.elee.even.sys_exc', 9)

    def get_counters(self):
        return str(counters)

    def fusion_alt(self, num):
        return '%s from fusion_alt' % num

    @alternative("arch.elee", ArgsSystemException, fusion_alt)
    def fusion_test(self, num):
        if not num % 2:
            return '%s from fusion_test' % num
        else:
            raise_system_exc(0)

    def signal(self, num):
        class namespace:
            pass
        namespace.func_name = 'TEST'
        namespace.logger = logger
        if num == 0:
            signals.alt_after_api_health_tested.send(namespace)
        elif num == 1:
            signals.alt_after_api_health_tested_bad.send(namespace)
        elif num == 2:
            signals.alt_after_api_health_locked.send(namespace)
        else:
            signals.alt_after_api_health_unlocked.send(namespace)
