# first of all import the socket library 
import socket, RSA

private_key_B = 100093193
public_key_KDA = 199570405


s = socket.socket()          
port = 2001       
s.bind(('', port))         
  
# put the socket into listening mode 
s.listen()      
print ("socket is listening")            
  
# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to A')  	
message = str(c.recv(1024))
print (message)
c.send(b'Received request from A')
# Close the connection with the A 
c.close() 
s.close()



# Connecting with KDA
port = 1001
s = socket.socket()          
s.connect(('192.168.59.49', port))
# Asking for public key of A 
s.send(b'Asking public key of A')
message = str(s.recv(1024))
# Closing connection with KDA
s.close()



# Connecting with A again
s = socket.socket()          
port = 12345
s.connect(('192.168.32.233', port))
# Talking to A
print ('Sending confirmation to A')
s.send(b'Asking for confirmation')
message = str(s.recv(1024))
print (message)
print ('Received confirmation of A')
s.send(b'Message 1 from B')
# Closing Connection with A
s.close()

