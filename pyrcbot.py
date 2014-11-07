import socket
#command sequence is currently hardcoded to "mb"
server=raw_input("What server? ").strip(" ")
channel=raw_input("Please enter the channel to join: ")
nick = raw_input("Bot Nickname?: ")
nspass=raw_input("Please enter the NickServ password ")
opname=raw_input("What name are you using on the chat? (Capitalization matters!) ")
conn=socket.socket()
def hi(name):#chan, name)#, message):
    #namend=message.find("!")
    #conn.send("PRIVMSG "+channel+" :Hi!\n")
    conn.send("PRIVMSG "+channel+" :Hello, "+name+"!\n")
def ping():
    conn.send("PONG "+":nick\n")
def quit():
    conn.send("QUIT\n")
    conn.close()
def part(channel):
    conn.send("PART "+channel+"\n")
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
    auth=recieved.find(opname,0,recieved.find("!"))
    if flag==0 and recieved.find("MODE")!=-1:
        conn.send("PRIVMSG NickServ :IDENTIFY "+nspass+"\n")
        conn.send("JOIN "+channel+"\n")
        flag=1
    if recieved.find("PING")!=-1:
        ping()
    if ":mb hi" in recieved:
        namend=recieved.find("!")
        name=recieved[1:namend]
	print name
        #chan=recieved.find("#")
	#conn.send("PRIVMSG "+channel+" :"+"Whoo\n")
        hi(name)#channel, recieved)
    if ":mb join" in recieved:
        eom=recieved.find("mb join")
        part(channel)
        channel=recieved[recieved.find("#",eom):recieved.find("\n")]#recieved.find(" ",eom)]
        join(channel)
   # if recieved.find(":mb test")!=-1:
    #    conn.send("PRIVMSG "+channel+ " :Hello\n")
    if ":mb quit" in recieved:
        quit()
        break
conn.close()

