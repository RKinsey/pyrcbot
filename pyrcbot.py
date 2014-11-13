import socket
#Auth is NOT secure. Anyone who knows the code can fake it
#I'll fix it after I learn regexes (will probably happen after the rewrite)
#Command sequence is currently hardcoded to "mb"
server=raw_input("What server? ").strip(" ")
channel=raw_input("Please enter the channel to join: ")
nick = raw_input("Bot Nickname?: ")
nspass=raw_input("Please enter the NickServ password ")
opname=(raw_input("What USERNAME(!) are you using on the chat? ")).lower()

conn=socket.socket()
def hi(name):
    conn.send("PRIVMSG "+channel+" :Hello, "+name+"!\n")
def ping():
    conn.send("PONG "+":nick\n")

def quit():
    conn.send("QUIT\n")
    conn.close()

def part(channel):
    conn.send("PART "+channel+"\n")

def join(recieved):
    start=recieved.find("#")
    end=recieved.find(" ",start)
    chan=recieved[start:end]
    conn.send("JOIN "+chan+"\n")

conn.connect((server,6667))
conn.send("NICK "+nick+"\n")
conn.send("USER pyrcbot pyrcbot pyrcbot :pyrcbot\n")


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
        hi(name)
    if ":mb join" in recieved:
        eom=recieved.find("mb join")
        part(channel)
        channel=recieved[recieved.find("#",eom):recieved.find("\n")]
        join(channel)
    if ":mb quit" in recieved and opname in (recieved[recieved.find("!"):recieved.find("@")]).lower():
	quit()
        break

conn.close()

