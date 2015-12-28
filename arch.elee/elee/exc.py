# -*- coding: utf-8 -*-

from . import thrift_file

ArgsErrorCode = thrift_file.ArgsErrorCode
ArgsSystemException = thrift_file.ArgsSystemException
ArgsUserException = thrift_file.ArgsUserException

TRANSLATIONS = {
    ArgsErrorCode.UNKNOWN_ERROR: u"系统异常，请稍后再试",
    ArgsErrorCode.DATABASE_ERROR: u"数据库错误",
    ArgsErrorCode.TOO_BUSY_ERROR: u"系统繁忙，请稍后再试",
}

def raise_system_exc(err_code, err_msg=None):
    """
    Raise SystemException which error message shall be hide from to user.

    :param err_code: Error code defined in thrift.
    """
    raise ArgsSystemException(
        err_code,
        ArgsErrorCode._VALUES_TO_NAMES[err_code],
        err_msg or "")


def raise_user_exc(err_code, err_msg=None):
    """
    Raise UserException which error message shall be show to user.

    :param err_code: Error code defined in thrift.
    """
    translation = err_msg or TRANSLATIONS[err_code]
    raise ArgsUserException(
        err_code,
        ArgsErrorCode._VALUES_TO_NAMES[err_code],
        translation)
