import unittest

from utils.HTMLTestRunner import HTMLTestRunner
class MytestCase(unittest.TestCase):
    def test0(self):
        print('当然')

    def test1(self):
        print('test1')

suit = unittest.TestSuite()
# suit1 = unittest.defaultTestLoader(uuuu,)

suit.addTest(unittest.makeSuite(MytestCase))

with open('./reports/登陆测试','wb') as f:
    runner = HTMLTestRunner(stream=f,tittle='***',description='***')
    runner.run(suit)