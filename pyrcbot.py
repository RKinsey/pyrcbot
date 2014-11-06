import socket

channel="#DesertBusBunker"
nick = "MoatBort"

conn=socket.socket()
conn.connect(("178.62.119.156",6667))
conn.send("PASS secret\n")
conn.send("NICK "+nick+"\n")
conn.send("USER moatbot moatbot moatbot :learning\n")

count=0
while count<10:
    recieved=conn.recv(1024)
    print recieved
    if recieved.find("PING :")!=-1:
        conn.send("PONG :pingis\n")
    count+=1
conn.send("JOIN "+channel+"\n")
conn.send("PRIVMSG "+channel+" :"+"Whoo\n")

conn.send("QUIT :done\n")
conn.close()

