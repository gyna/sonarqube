# main_test.py에 추가할 내용

# 기존 import 구문들...
from main import add_numbers
from NewFile import process_user_data # NewFile.py에서 함수를 가져옵니다.

# 기존 테스트 함수...
def test_simple_addition():
    assert add_numbers(5, 10) == 15

# NewFile.py를 위한 새로운 테스트 함수 추가
def test_process_user_data_long():
    # 긴 데이터에 대한 테스트
    result = process_user_data(["a", "b", "c", "d", "e", "f"])
    assert result == "Long data processed"

def test_process_user_data_short():
    # 짧은 데이터에 대한 테스트
    result = process_user_data(["a", "b"])
    assert result == "Short data processed"

def test_connection_details():
    details = get_connection_details()
    # 함수가 올바른 IP와 포트를 반환하는지 테스트합니다.
    assert details["ip"] == "192.168.1.10"
    assert details["port"] == 8080
