import socket 

# 접속할 서버 주소
HOST = '127.0.0.1'
# 클라이언트 접속을 대기하는 포트 번호
PORT = 9999        

# 학점계산 함수 Grade 정의
def Grade(score):
    if score < 50:
        print("F")
    elif score < 60:
        print("D0")
    elif score < 65:
        print("D+")
    elif score < 70:
        print("C0")
    elif score < 75:
        print("C+")
    elif score < 80:
        print("B0")
    elif score < 85:
        print("B+")
    elif score < 95:
        print("A0")
    else:
        print("A+")
    
# 소켓 생성
# 주소 체계 : IPv4, 소켓 타입 : TCP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는 WinError 10048 에러 해결
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind - 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용
server_socket.listen()

print('server start')

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴 
connectionSock, addr = server_socket.accept()

# 접속한 클라이언트의 주소 print
print('Connected by', addr)

# 무한루프(while문) 
while True:
    # 클라이언트가 보낸 점수를 수신 
    num = connectionSock.recv(1024)
    # 받은 점수를 학점계산 함수인 Grade로 계산
    Grade(int(num))
    # 나온 학점을 입력
    grade = input('Grade : ')

    # 빈 문자열을 수신하면 루프 중지
    if not num:
        break
    
    # 수신받은 문자열을 출력
    print('Received from', addr, num)

    # 받은 문자열을 다시 클라이언트로 전송 (에코) 
    connectionSock.send(grade.encode())

# 소켓 닫기
connectionSock.close()
server_socket.close()