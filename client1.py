import socket
import time

server_ip = 'localhost'  # 위에서 설정한 서버 ip
server_port = 3333  # 위에서 설정한 서버 포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))


def checkalive():
    msg = 'Are you alive?'
    socket.sendall(msg.encode(encoding='utf-8'))
    print(msg)


start = time.time()
socket.settimeout(10)  # 서버의 응답을 기다리는 시간`
cnt = 0

while True:
    #서버가 요청을 3번이나 보냈는데 응답이 없을 때 문제있는것으로 인식
    if cnt == 4:
        print("sever is fault")
        print(int(time.time() - start),"초")
        print()
        break
    checkalive()  # 메세지 전송
    try:
        data = socket.recv(1024)  # 서버가  보낸 메시지를 클라이언트가 받음
    except:
        cnt += 1
        print("no data")
        print(cnt)
        print(int(time.time() - start),"초")
        print()
        continue
    msg = data.decode()  # 읽은 데이터 디코딩
    print('server: ', msg)
    print(int(time.time() - start),"초")
    print()
    time.sleep(10)  # 메세지 보내는 주기 설정

socket.close()
