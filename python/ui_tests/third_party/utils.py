"""
-----
Utils
-----
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import uuid

__all__ = [
    'generate_ids',
    'get_unwrapped_func',
    'slugify',
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


def generate_ids(prefix=None, postfix=None, count=1):
    """Generate unique IDs."""
    for _ in range(count):
        result = 'a' + str(uuid.uuid4())[:8]
        if prefix:
            result = prefix + result
        if postfix:
            result += postfix
        yield result
