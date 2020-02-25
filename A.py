import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
s.send(b'Connection request of B')
message = s.recv(1024)
print (message)
print ('Got public key of B') 

# close the connection 
s.close()

port_b = 12346

s.connect(('127.0.0.1', port))

s.send(b'Sending message to B')
s.close()


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
print ('Connected to B') 

print ('received confirmation from B')

c.send(b'Sending confirmation to B')

message = str(c.recv(1024))
print (message)

c.close()
