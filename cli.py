import socket

# 접속할 서버 주소
HOST = '127.0.0.1'  
# 서버에서 지정해 놓은 포트 번호 
PORT = 9999       

# 소켓 생성
# 주소 체계 : IPv4, 소켓 타입 : TCP 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 접속
client_socket.connect((HOST, PORT)) 

# 무한루프(while문)
while True: 
    # 점수 입력
    score = input('Enter score ( Q / q = quit) : ')
    # q나 Q입력시 종료
    if score == 'q' or score == 'Q':
        break
    
    # 메시지를 전송합니다.
    client_socket.send(score.encode())
    # 서버가 보낸 학점 수신
    data = client_socket.recv(1024)
    
    #메세지 수신
    print('YOUR GRADE : ',repr(data.decode()))

#소켓 닫기
client_socket.close()