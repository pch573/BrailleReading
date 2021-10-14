import Translation
import socket


host='192.168.35.49'
port=9990
ADDR=(host,port)

server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(ADDR)
server_sock.listen(1)
print("%d번포트로접속기다리는중..."%port)

client_sock,addr=server_sock.accept()


print(str(addr),'Connectedby')
msg=Translation.com
print(msg.encode("utf-8"))

while True:
        client_sock.send(msg.encode("utf-8"))

        recvdata=client_sock.recv(1024)
        print('상대방:',recvdata.decode("utf-8"))



client_sock.close()
server_sock.close()
