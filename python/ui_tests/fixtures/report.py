"""
---------------
Report fixtures
---------------
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

import logging
import logging.config
import os

import allure
import pytest
import yaml

from ui_tests import config
from ui_tests.third_party import utils

__all__ = [
    'report_log',
    'report_dir',
]


@pytest.fixture
def report_dir(request):
    """Create report directory.

    Args:
        request (object): pytest request

    Returns:
        str: path to report directory
    """
    _report_dir = os.path.join(config.TEST_REPORTS_DIR,
                               utils.slugify(request._pyfuncitem.name))

    if not os.path.isdir(_report_dir):
        os.makedirs(_report_dir)

    return _report_dir


@pytest.yield_fixture(autouse=True)
def report_log(report_dir):
    """Configure log handlers to write test logs.

    Args:
        report_dir (str): path to report directory
    """
    log_path = os.path.join(report_dir, 'called_functions.log')
    yaml_path = os.path.join(os.path.dirname(__file__), 'logging.yaml')
    with open(yaml_path) as file:
        log_content = file.read().format(FILE_PATH=log_path)
    logging.config.dictConfig(yaml.safe_load(log_content))

    yield

    with open(log_path) as log_file:
        allure.attach('called functions',
                      log_file.read(),
                      allure.attach_type.TEXT)
