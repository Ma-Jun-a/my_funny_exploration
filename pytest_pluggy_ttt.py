import requests
import os
import json


class UploadAllureResult(object):
    def __init__(self, allure_result_path, upload_url):
        self.allure_result_path = allure_result_path
        self.upload_url = upload_url

    def get_file_name(self):
        '''
        获取制定目录下的所有文件名
        :return:
        '''
        for root, dirs, files in os.walk(self.allure_result_path):
            self.dirs = dirs  # 当前路径下所有子目录,root 当前目录路径
            self.files = files  # 当前路径下所有非目录子文件

    def upload_allure_result(self):
        '''
        上传指定文件
        :return:
        '''
        label = self.get_label()
        if label == '':
            label = self.get_label()

        for allure_result_file in self.files:
            allure_result_file_path = os.path.join(self.allure_result_path, allure_result_file)
            file = {
                'file': open(allure_result_file_path, 'rb'),

            }

            url = self.upload_url + '?label=' + label
            requests.post(url, files=file)

    def get_label(self):
        # label_path = os.path.join('D:\UI_case\scripts', "label.txt")
        label_path = os.path.join(os.getcwd(), "label.txt")
        print('label_path:', label_path)
        with open(label_path, "r") as f:
            label = f.read()
            print('get_label:', label)
            return label


class CollectTestCasePlugin(object):
    collected_result = {'totalScripts': 0, 'otherScripts': 0}

    def __init__(self, config):
        self.config = config

    def pytest_collection_finish(self, session):
        if self.config.option.collectTestCase:
            self._printcollecteditems(session.items)

    def _printcollecteditems(self, items):

        self.collected_result['totalScripts'] = len(items)

        for item in items:  # 所有的脚本数据

            item_node_id_str = item.nodeid
            index = item_node_id_str.find('/')
            if index >= 0:
                module_name = item_node_id_str[:index]
                if module_name in self.collected_result:
                    self.collected_result[module_name] = self.collected_result[module_name] + 1
                else:
                    self.collected_result[module_name] = 1
            else:
                self.collected_result['otherScripts'] = self.collected_result['otherScripts'] + 1
        print(self.collected_result)

    def pytest_runtestloop(self, session):

        if session.config.option.collectTestCase:
            return True


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        '--collectTestCase', action='store_true', dest="collectTestCase",
        help="collect test case")


def pytest_configure(config):
    if config.option.collectTestCase:
        config.pluginmanager.register(CollectTestCasePlugin(config), "collectTestCase")
        # 使用方式：在脚本文档中将conftest文件放进去，（前提：已安装pytest），然后在任意脚本中执行 pytest --collectTestCase