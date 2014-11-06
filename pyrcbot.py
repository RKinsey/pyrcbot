import socket
#server="irc.chatspike.net"
channel="#DesertBusBunker"
nick = "MoatBot"
conn=socket.socket()
conn.connect(("178.62.119.156",6667))
conn.send("PASS 14620\n")
conn.send("NICK "+nick+"\n")
conn.send("USER moatbot moatbot moatbot :learning\n")
conn.send("JOIN "+channel+"\n")
conn.send("PRIVMSG "+channel+" :"+"Whoo\n")
 
while 1:
    recieved=conn.recv(1024)
    print recieved
conn.close()

