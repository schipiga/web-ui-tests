"""
-----------
Application
-----------
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

import re
import urlparse

import pom
from pom import ui
from pom.base import camel2snake
from selenium.webdriver.remote.remote_connection import RemoteConnection

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_tests import config
from ui_tests.app import pages

__all__ = [
    'Application',
]

ui.UI.timeout = config.UI_TIMEOUT
RemoteConnection.set_timeout(config.ACTION_TIMEOUT)


@pom.register_pages(pages.pages)
class Application(pom.App):
    """Application to launch in browser."""

    driver_path = ChromeDriverManager().install()
    driver_path = GeckoDriverManager().install()

    def __init__(self, url, *args, **kwgs):
        """Constructor."""
        super(Application, self).__init__(
            url, browser='firefox', executable_path=self.driver_path,
            *args, **kwgs)

        self.webdriver.maximize_window()
        #self.webdriver.set_window_size(*config.RESOLUTION)
        self.webdriver.set_page_load_timeout(config.ACTION_TIMEOUT)
        self.webdriver.get(self.app_url)

    @property
    def current_page(self):
        """Define current page"""
        current_path = urlparse.urlparse(self.webdriver.current_url).path
        for page in self._registered_pages:
            if re.match(page.url, current_path):
                return getattr(self, camel2snake(page.__name__))
        else:
            raise Exception("Can't define current page")

    def open(self, page):
        """Open page or url.
        Args:
            page (PageBase|str): page class or url string.
        """
        url = page if isinstance(page, str) else page.url
        super(Application, self).open(url)

    def flush_session(self):
        """Delete all cookies.
        It forces flushes user session by cookies deleting.
        """
        self.webdriver.delete_all_cookies()
