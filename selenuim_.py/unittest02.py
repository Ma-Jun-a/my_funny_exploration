import unittest
from ceshiyongli import YouTestCase,MyTestCase

suite = unittest.TestSuite()

suite.addTest(YouTestCase.hetest2_1)
suite1 = unittest.TestSuite()
suite1.addTest(unittest.makeSuite(MyTestCase))
suite2 = unittest.defaultTestLoader.discover(testdir,pattern='test**')

runner = unittest.TextTestRunner()
runner.run(suite)
