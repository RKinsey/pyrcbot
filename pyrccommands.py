def hi(name):#chan, name)#, message):
    #namend=message.find("!")
    #conn.send("PRIVMSG "+channel+" :Hi!\n")
    conn.send("PRIVMSG "+channel+" :Hello, "+name+"!\n")
def ping(conn):
    conn.send("PONG "+":nick\n")
def quit(conn):
    conn.send("QUIT\n")
    conn.close()
def part(conn,channel):
    conn.send("PART "+channel+"\n")
def join(conn,msg):
    start=msg.find("#")
    end=msg.find(" ",start)
    chan=msg[start:end]
    conn.send("JOIN "+chan+"\n")
def commands(conn,msg):
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