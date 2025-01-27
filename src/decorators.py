from functools import wraps
from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[Any] = None) -> Any:
    """Создаем функцию-декоратор с параметром"""

    def decorator(func: Callable) -> Any:
        """Создаем вспомогательную функцию для формирования замыкания"""

        @wraps(func)
        def wrapper(*args: tuple[tuple, ...], **kwargs: dict[str, Any]) -> Any:
            """Создаем замыкание"""
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"{func.__name__} started at {start_time}\n"
                            f"{func.__name__} finished at {end_time}\n"
                            f"{func.__name__} ok, result: {result}\n"
                        )
                else:
                    print(
                        f"{func.__name__} started at {start_time}\n"
                        f"{func.__name__} finished at {end_time}\n"
                        f"{func.__name__} ok, result: {result}\n"
                    )
                return result
            except Exception as e:
                end_time = time()
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"{func.__name__} started at {start_time}\n"
                            f"{func.__name__} finished at {end_time}\n"
                            f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                        )
                else:
                    print(
                        f"{func.__name__} started at {start_time}\n"
                        f"{func.__name__} finished at {end_time}\n"
                        f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                    )
                raise e

        return wrapper

    return decorator
