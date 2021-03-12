import pytest


@pytest.fixture()
def before1():
    print('before1 test')

class Test_01(object):
    def test_01(self,before1):
        print('test01')
        assert 1
    def test_02(self):
        print('test02')
        assert 1
