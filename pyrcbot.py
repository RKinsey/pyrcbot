import socket
#command sequence is currently mb
server="irc.chatspike.net"
channel="#DesertBusBunker"
nick = "MoatBot"
nspass=raw_input("please enter your NS password")
#server=raw_input("What server?")
#channel=raw_input("Please enter the channel to join")
#nick = raw_input("Bot Nickname?")
#nspass=raw_input("Please enter the nickServ password")

conn=socket.socket()
conn.connect((server,6667))
conn.send("PASS secret\n")
conn.send("NICK "+nick+"\n")
conn.send("USER moatbot moatbot moatbot :learning\n")
flag=0
while True:
    recieved=conn.recv(1024)
    print recieved
    if flag==0 and recieved.find("MODE")!=-1:
        conn.send("PRIVMSG NickServ :IDENTIFY "+nspass+"\n")
        conn.send("JOIN "+channel+"\n")
        flag=1
    if recieved.find(":mb test")!=-1:
        conn.send("PRIVMSG "+channel+ " :Hello\n")
    if recieved.find(":mb quit")!=-1:
        conn.send("QUIT :leaving")
        break
    

conn.close()

