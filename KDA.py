# first of all import the socket library 
import socket, RSA

private_key_KDA = 1001629
public_key_A = 1893307107
public_key_B = 1841622505



  
s = socket.socket()          
print ("Socket successfully created")
  

port = 1001
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  

s.listen()      
print ("socket is listening")            
  
# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to A')  	
message = str(c.recv(1024))
print (message)
c.send(b'Sending public key of B')
# Close the connection with the A
c.close()


# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to B')  	
message = str(c.recv(1024))
print (message)
c.send(b'Sending public key of A')
# Close the connection with the A
c.close()
