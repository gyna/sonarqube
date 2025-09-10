import os

# 1. 보안 취약점 (Vulnerability): 비밀번호를 소스코드에 하드코딩
db_password = "my_super_secret_password_123"

def process_user_data(data):
    # 2. 버그 (Bug): 변수를 선언했지만 사용하지 않음
    is_processed = True

    if len(data) > 5:
        print("Processing long data...")
        # 3. 코드 냄새 (Code Smell): 아래 로직이 거의 동일하게 중복됨
        for item in data:
            print(f"Item: {item}")
        return "Long data processed"
    else:
        print("Processing short data...")
        # 3. 코드 냄새 (Code Smell): 위 로직과 거의 동일하게 중복됨
        for item in data:
            print(f"Item: {item}")
        return "Short data processed"

def process_admin_data(data):
    if len(data) > 5:
        print("Processing other long data...")
        # 3. 코드 냄새 (Code Smell): 위 함수와 로직이 거의 동일하게 중복됨
        for item in data:
            print(f"Item: {item}")
        return "Other long data processed"
    else:
        print("Processing other short data...")
        # 3. 코드 냄새 (Code Smell): 위 함수와 로직이 거의 동일하게 중복됨
        for item in data:
            print(f"Item: {item}")
        return "Other short data processed"

process_user_data(["a", "b", "c", "d", "e", "f"])
process_admin_data(["x", "y", "z"])
