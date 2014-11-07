import socket
#command sequence is currently hardcoded to "mb"
server=raw_input("What server? ")
channel=raw_input("Please enter the channel to join: ")
nick = raw_input("Bot Nickname?: ")
nspass=raw_input("Please enter the NickServ password ")
opname=raw_input("What name are you using on the chat? (Capitalization matters!) ")
conn=socket.socket()
def hi(chan, message):
    namend=message.find("!")
    conn.send("PRIVMSG "+chan+" :Hi!"
#    this doesn't work
    #conn.send("PRIVMSG "+chan+" :Hello, "+message[0:namend]+"!\n")
def ping():
    conn.send("PONG "+"nick")
def quit():
    conn.send("QUIT\n")
    conn.close()
def join(msg):
    start=msg.find("#")
    end=msg.find(" ",start)
    chan=msg[start:end]
    conn.send("JOIN "+chan+"\n")
conn.connect((server,6667))
#conn.send("PASS secret\n")
conn.send("NICK "+nick+"\n")
conn.send("USER pyrcbot pyrcbot pyrcbot :pyrcbot\n")
#conn.send("PRIVMSG NickServ :IDENTIFY "+nspass+"\n")
#conn.send("JOIN "+channel+"\n")

flag=0
while True:
    recieved=conn.recv(1024)
    print recieved
    if flag==0 and recieved.find("MODE")!=-1:
        conn.send("PRIVMSG NickServ :IDENTIFY "+nspass+"\n")
        conn.send("JOIN "+channel+"\n")

        flag=1
    if recieved.find("PING")!=-1:
        ping()
    if recieved.find(":mb hi")!=-1: 
        chan=recieved.find("#")
        hi(channel, recieved)
    if recieved.find(":mb join")!=-1 and recieved.find(opname,0,20)!=-1:
	join(recieved)
   # if recieved.find(":mb test")!=-1:
    #    conn.send("PRIVMSG "+channel+ " :Hello\n")
    if recieved.find(":mb quit")!=-1 and recieved.find(opname,0,20)!=-1:
        quit()
        break

conn.close()

