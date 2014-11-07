pyrcbot
=======

Simple Python IRC bot.  

To do:  
Convert to using Twisted (Have to finish learning it first)  
Modularity? 

NOTE: Does not work with all IRC servers! Darkmyst is the only one I've found so far.
It won't accept PRIVMSG commands & returns "No text to send" followed by "Unknown command". I'm not sure why this is, and I can't pull enough data to find out.
Also, the code needs to be modified if the server expects PONG to send the exact data the PING sent. This is pretty trivial and only takes a few lines of code.
