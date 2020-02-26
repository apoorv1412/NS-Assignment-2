# first of all import the socket library 
import socket, RSA

private_key_B = 100093193
public_key_KDA = 199570405
public_key_A = -1
ID_A = -1

def format(msg):
	return msg.split('||')


s = socket.socket()          
port = 2002   
s.bind(('', port))         
  
# put the socket into listening mode 
s.listen()      
print ("socket is listening")            
  
# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to A')  	
request_from_A_encrypted = c.recv(1024).decode()
request_from_A_decrypted = RSA.decrypt(request_from_A_encrypted, RSA.n, private_key_B)
formatted_message = format(request_from_A_decrypted)
ID_A = formatted_message[0]

print('Received request from A')
print (ID_A)
# Close the connection with the A 
c.close() 
s.close()



# Connecting with KDA
port = 10002
s = socket.socket()          
s.connect(('192.168.32.218', port))
# Asking for public key of A 
print('Asking public key of A')
request_to_KDA = 'Connection request to A' + '||' + '.'
s.send(request_to_KDA.encode())
reply = s.recv(1024).decode()
decrypted_reply = RSA.decrypt(reply, RSA.n, public_key_KDA)
public_key_A = int(format(decrypted_reply)[0])
print('Got public key of A', public_key_A)
# Closing connection with KDA
s.close()



# # Connecting with A again
# s = socket.socket()          
# port = 12345
# s.connect(('192.168.32.233', port))
# # Talking to A
# print ('Sending confirmation to A')
# s.send(b'Asking for confirmation')
# message = str(s.recv(1024))
# print (message)
# print ('Received confirmation of A')
# s.send(b'Message 1 from B')
# # Closing Connection with A
# s.close()

