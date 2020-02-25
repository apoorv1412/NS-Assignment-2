# first of all import the socket library 
import socket                
  
# next create a socket object 
s = socket.socket()          
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12346              
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
  
# put the socket into listening mode 
s.listen()      
print ("socket is listening")            
  
# Establish connection with client. 
c, addr = s.accept()      
print ('Connected to A')  	

message = str(c.recv(1024))
print (message)
c.send(b'Received request from A')
# Close the connection with the client 
c.close() 

port = 12345
s.connect(('127.0.0.1', port))

s.send(b'Asking public key of A')

s.close()

port = 12345

s.connect(('127.0.0.1', port))
print ('Sending confirmation to A')
s.send(b'Asking for confirmation')

message = str(s.recv(1024))
print (message)

print ('Received confirmation of A')

s.send(b'Message 1 from B')

s.close()

