'''
Created on Apr 23, 2021

@author: flba
'''
import time
import gspread
from functools import wraps


def open_spreadheet(sheet_name):
    client = gspread.service_account(filename="data/service_account_cred.json")
    return client.open(sheet_name).sheet1


def timestamp():
    return time.perf_counter()


def retry_until_func_passes(timeout,
                            retry_interval,
                            exceptions=(Exception)):

    def wait_until_passes_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = timestamp()
            while True:
                try:
                    func_val = func(*args, **kwargs)
                    break
                except exceptions as e:
                    time_left = timeout - (timestamp() - start)
                    if time_left > 0:
                        time.sleep(min(retry_interval, time_left))
                    else:
                        err = TimeoutError()
                        err.original_exception = e
                        raise err
            return func_val

        return wrapper

    return wait_until_passes_decorator
