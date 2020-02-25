# first of all import the socket library 
import socket                
  
# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen()      
print ("socket is listening")            
  
# Establish connection with client. 
c, addr = s.accept()      
print ('Connected to A')  	

message = str(c.recv(1024))
print (message)
c.send(b'Sending public key of B')
# Close the connection with the client 
c.close() 
