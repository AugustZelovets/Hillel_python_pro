from typing import Union


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function "{func.__name__}",',
              'args:', args if len(args) > 0 else '',
              'kwargs:', kwargs if len(kwargs) > 0 else '')
        return func(*args, **kwargs)

    return wrapper


@decorator
def add(a: Union[int, float], b: Union[int, float], c) -> Union[int, float]:
    return a + b


add(1, 2, c=3)
