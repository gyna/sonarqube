import socket

def get_connection_details():
    # 보안 핫스팟: IP 주소가 소스코드에 하드코딩되어 있습니다.
    # 환경이 변경되면 코드를 직접 수정해야 하므로 좋지 않은 방식입니다.
    host_ip = "192.168.1.10" # SonarQube가 이 부분을 지적할 것입니다.
    port = 8080
    
    return {"ip": host_ip, "port": port}

def add_numbers(a, b):
    return a + b
