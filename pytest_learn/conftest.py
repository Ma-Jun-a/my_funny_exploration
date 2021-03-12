import pytest
import os

from py._xmlgen import html
from selenium import webdriver
import time
# pytest_plugins = ("myapp.testsupport.myplugin",)
# 1. 测试结束后自动打开html文件
# def open_url_in_browser(url):
#     firefox = webdriver.Firefox()
#     firefox.get(url)
#     time.sleep(40)
#     firefox.close()
#
# @pytest.hookimpl(trylast=True)
# def pytest_configure(config):
#     config._htmlfile = config._html.logfile
#
# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(session, exitstatus):
#     file = session.config._htmlfile
#     # invoke the file opening in external tool
#     os.system('open' + file)
#
# def pytest_unconfigure(config):
#     html_report_path = os.path.join(config.invocation_dir.strpath, config.option.htmlpath)
#     open_url_in_browser("file://%s" % html_report_path)

from datetime import datetime

import pytest
# 增加html报告的用例描述字段
from datetime import datetime
import pytest

# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(1, html.th('Time', class_='sortable time', col='time'))
#     cells.pop()
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop()
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# 使得每个测试都能够使用该方法
class DB:
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()
    def __str__(self):
        return "DBduixinglianfjie"

db = DB()
@pytest.fixture(autouse=True)
def db():
    return DB()
@pytest.fixture()
def pretest():
    print("before function ")
    # db.begin(request.function.__name__)
    yield
    print("after function")
    # db.rollback()

# class TestClass:
#     @pytest.fixture(autouse=True)
#     def transact(self, request, db):
#         db.begin(request.function.__name__)
#         yield
#         db.rollback()
#
#     def test_method1(self, db):
#         assert db.intransaction == ["test_method1"]
#
#     def test_method2(self, db):
#         assert db.intransaction == ["test_method2"]


