import pytest

@pytest.fixture()
def before():
    print('before test')
@pytest.mark.usefixtures('before')
class Test_01(object):
    def test_01(self):
        print('test01')
        assert 1
    def test_02(self):
        print('test02')
        assert 1
