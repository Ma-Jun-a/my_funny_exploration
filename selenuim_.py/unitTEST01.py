import unittest


class MytestCase(unittest.TestCase):
    def test0(self):
        print('当然')

    def test1(self):
        print('test1')


class YouTestCase(unittest.TestCase):
    def test2_1(self):
        print('2-1')

    def test2_2(self):
        print('2-2')


# if __name__ == '__main__':
#     unittest.main()