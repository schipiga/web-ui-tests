.. web ui tests documentation master file, created by
   sphinx-quickstart on Sat Mar 11 20:35:18 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================================
Welcome to web ui tests's documentation
=======================================

----------
Annotation
----------

This project includes some e2e test scenarios for web UI application via STEPS-architecture. As target project is used https://pipedrive.com.
It uses next toolkits:

- ``pytest`` (http://docs.pytest.org) - the best python testing framework
- ``python-pom`` (http://pom.readthedocs.io) - tiny wrapper over selenium
- ``xvfb`` (https://en.wikipedia.org/wiki/Xvfb) - virtual display to launch tests in headless mode (disabled by default)
- ``libav`` (https://libav.org) - audio and video processing toolkit to capture video of display (disabled by default)
- ``pytest-xdist`` (https://pypi.python.org/pypi/pytest-xdist) - plugin to launch tests in parallel mode (disabled by default) 

It also requires next installed software:

- ``google-chrome``
- ``firefox``
- ``xvfb`` (optional, linux only)
- ``libav`` (optional, linux only)

It's verified on **ubuntu v16.04**, **chrome v57** and **firefox v52**.

.. ATTENTION::
    There are some flaky troubles with firefox since they migrated on geckodriver. According to its opened `issues <https://github.com/mozilla/geckodriver/issues>`_ list, it's not fully stable.

--------------
How to install
--------------

Execute in shell next commands::

    $ git clone https://github.com/sergeychipiga/web-ui-tests
    $ cd web-ui-tests/python
    $ virtualenv .venv
    $ . .venv/bin/activate
    $ pip install -r requirements.txt

-------------------
How to launch tests
-------------------

Execute in shell next command::

    $ py.test

By default it launches tests in **google-chrome**. To specify **firefox** execute command::

    $ py.test --browser firefox

To capture video::

    $ py.test --enable-video-capture

To launch tests in virtual display with video capture::

    $ py.test --enable-video-capture --enable-virtual-display

To launch tests in virtual display with video capture in parallel mode::

    $ py.test --enable-video-capture --enable-virtual-display -n 2

-----------------
How to get report
-----------------

Please be sure that you have installed `allure-cli <http://wiki.qatools.ru/display/AL/Allure+Commandline>`_.
Then after tests finishing execute in terminal next commands::

    $ allure generate allure-results -o allure-report
    $ allure report open --report-dir allure-report -p 20000

Then new browser window will be opened and navigation to local URL with report happens.
If navigation doesn't happen by default, you can open it manually http://localhost:20000/.

To clear previous reports execute::

    $ rm -rf allure-* test_*

------------------
Project components
------------------

.. toctree::
    :maxdepth: 1

    web_app
    steps
    fixtures
    tests
    third_party
