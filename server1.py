import time,socket,sys
print("\nWelcome to chat room")
print("Initialising.......")
time.sleep(1)
s=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)
port=1234
s.bind((host,port))
print(host,"(",ip,")\n")
name=input(str("Enter your name..."))
s.listen(1)
print("\n waiting for incoming connection.....")
conn,addr=s.accept()
print("\n Recevied connection from",addr[0],"(",addr[1])
s_name=conn.recv(1024)
s_name=s_name.decode()
print(s_name,"has connected to the chat room")
conn.send(name.encode())
while True:
    message=input(str("Me: "))
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(s_name,":",message)
