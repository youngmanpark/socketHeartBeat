import socket
import time

host = 'localhost'
port = 3333

# 서버 소켓 오픈
# socket.AF_INET: 주소 종류 지정(IP) / socket.SOCK_STREAM: 통신 종류 지정(TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.SOL_SOCKET: 소켓 옵션
# SO_REUSEADDR: 현재 사용 중인 ip/ 포트번호를 재사용 할 수 있다.
# 커널이 소켓을 사용 하는 중에도 계속 해서 사용할 수 있다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server socket 에 ip와 port 를 붙여줌(bind)
server_socket.bind((host, port))

# 접속 준비 완료
server_socket.listen()

# echo program: 입력한 값을 메아리 치는 기능(그대로 다시 보냄)
print(' server start ')

# accept(): 클라이언트 접속 기다리며 대기
# 클라이언트가 접속하면 서버-클라이언트 1:1 통신이 가능한 작은 소켓(client_soc)을 만들어서 반환
# 접속한 클라이언트의 주소(addr)역시 반환
client_soc, addr = server_socket.accept()

print('connect client addr: ', addr)
cnt=0

# recv(메시지 크기) :소켓에서 크기만큼 읽는 함수
# 소켓에 읽을 데이터가 없으면 생길 때까지 대기함
while True:

    data = client_soc.recv(1024)
    msg = data.decode()  # 읽은 데이터 디코딩
    print('recv msg: ', msg)
    if msg=="" :
        break
    cnt += 1
    if msg == 'Are you alive?':
        if cnt ==4:
            print("서버 강제로 다운")
            time.sleep(40)
        else:
            msg="yes I'm alive"
            client_soc.sendall(msg.encode(encoding='utf-8'))
            # 메세지 클라이언트로 보냄
server_socket.close()  # 사용한 서버 소켓 닫기
