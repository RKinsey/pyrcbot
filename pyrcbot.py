import socket
import pyrccommands
#command sequence is currently hardcoded to "mb"
server=raw_input("What server? ").strip(" ")
channel=raw_input("Please enter the channel to join: ")
nick = raw_input("Bot Nickname?: ")
nspass=raw_input("Please enter the NickServ password ")
opname=raw_input("What name are you using on the chat? (Capitalization matters!) ")
conn=socket.socket()

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
    commands(recieved)
conn.close()

