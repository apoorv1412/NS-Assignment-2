import socket         

'''
Sending request to KDA asking for public key of B
'''       
s = socket.socket()            
port = 1001             
s.connect(('192.168.59.49', port))
s.send(b'Connection request of B')
message = s.recv(1024)
print (message)
print ('Got public key of B') 
s.close()

'''
Sending message to B, asking for confirmation
'''
port = 2001
s = socket.socket()
s.connect(('192.168.32.232', port))
s.send(b'Sending message to B')
s.close()

'''
Listening to B's response
'''
port = 12345 
s = socket.socket()
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
s.listen()      
print ("socket is listening")            
c, addr = s.accept()      
print ('Connected to B') 
print ('received confirmation from B')
c.send(b'Sending confirmation to B')
message = str(c.recv(1024))
print (message)
c.close()
