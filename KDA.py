# first of all import the socket library 
import socket, RSA

def format(msg):
	return msg.split('||')

private_key_KDA = 1001629
public_key_A = 1893307107
public_key_B = 1841622505
  
s = socket.socket()          
print ("Socket successfully created")
  
port = 10003
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
s.listen()      
print ("socket is listening")            
  
# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to A')  	
request = c.recv(1024).decode()
formatted_request = format(request)[0]
print (formatted_request)
print ('Sending public key of B')
message = str(public_key_B) + '||' + request
encrypted_message = RSA.encrypt(message, RSA.n, private_key_KDA)
c.send(str.encode(encrypted_message))
# Close the connection with the A
c.close()

# Establish connection with B. 
c, addr = s.accept()      
print ('Connected to B')  	
request = c.recv(1024).decode()
formatted_request = format(request)[0]
print (formatted_request)
print ('Sending public key of A')
message = str(public_key_A) + '||' + request
encrypted_message = RSA.encrypt(message, RSA.n, private_key_KDA)
c.send(str.encode(encrypted_message))
# Close the connection with the A
c.close()

s.close()
