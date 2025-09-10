from main import add_numbers

# 'test_'로 시작하는 테스트 함수를 만듭니다.
def test_addition():
    # add_numbers(5, 10)의 결과가 15가 맞는지 확인(assert)합니다.
    assert add_numbers(5, 10) == 15
