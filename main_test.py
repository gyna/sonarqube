import unittest
from main import add_numbers  # main.py 파일에서 add_numbers 함수를 가져옵니다.

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        # 5와 10을 더하면 15가 맞는지 테스트합니다.
        self.assertEqual(add_numbers(5, 10), 15)

if __name__ == '__main__':
    unittest.main()
