import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.num = int(input("请输入你想要的数字："))

    def test_case(self):
        self.assertEqual(self.num, 5, "你输入的数字不是5")  # add assertion here

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
