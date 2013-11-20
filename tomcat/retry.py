import time, logging
from functools import wraps

def retry(exception, tries=4, delay=3, backoff=2, logger=None):
    """http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param exception: the exception to check.
    :param tries: number of times to try (not retry) before giving up
    :param delay: initial delay between retries in seconds
    :param backoff: backoff multiplier
    :param logger: logger to use. If None, print
    """
    def retry_decorator(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exception, e:
                    mtries -= 1
                    msg = "%s, %d attempts remaining, Retrying in %d seconds..." % (str(e), mtries, mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
                    time.sleep(mdelay)
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry

    return retry_decorator
