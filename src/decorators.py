import time
from functools import wraps


def log(filename=""):
    """Декоратор регистрирует детали выполнения функций"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if filename:
                with open(filename, "w", encoding="utf8") as file:
                    try:
                        start_time = time.time()
                        result = func(*args, **kwargs)
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        file.write(f"{func.__name__} {result} time: {elapsed_time}")
                    except Exception as e:
                        file.write(f"{func.__name__} error: {type(e).__name__}. Input: ({args}, {kwargs})")
            else:
                try:
                    start_time = time.time()
                    result = func(*args, **kwargs)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"{func.__name__} {result} time: {elapsed_time}")
                except Exception as e:
                    print(f"{func.__name__} error: {type(e).__name__}. Input: ({args}, {kwargs})")
            return result

        return inner

    return wrapper
