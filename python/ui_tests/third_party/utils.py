import inspect


__all__ = [
    'slugify',
    'get_unwrapped_func',
]


def slugify(string):
    """Replace non-alphanumeric symbols to underscore in string.
    Args:
        string (str): string to replace
    Returns:
        str: replace string
    """
    return ''.join(s if s.isalnum() else '_' for s in string).strip('_')


def get_unwrapped_func(func):
    """Get original function under decorator.

    Decorator hides original function inside itself. But in some cases it's
    important to get access to original function, for ex: for documentation.

    Args:
        func (function): function that can be potentially a decorator which
            hides original function

    Returns:
        function: unwrapped function or the same function
    """
    if not inspect.isfunction(func) and not inspect.ismethod(func):
        return func

    if func.__name__ != func.func_code.co_name:
        for cell in func.func_closure:
            obj = cell.cell_contents
            if inspect.isfunction(obj):
                if func.__name__ == obj.func_code.co_name:
                    return obj
                else:
                    return get_unwrapped_func(obj)
    return func
