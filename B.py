# first of all import the socket library 
import socket, RSA
from random import randint as rint

private_key_B = 100093193
public_key_KDA = 199570405
public_key_A = -1
ID_A = -1
nonce_sent_by_A = -1
nonce_B = -1

def format(msg):
	return msg.split('||')


s = socket.socket()          
port = 2004
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
nonce_sent_by_A = int(formatted_message[1])

print('Received request from A')
print (ID_A, nonce_sent_by_A)
# Close the connection with the A 
c.close() 
s.close()



# Connecting with KDA
port = 10003
s = socket.socket()          
s.connect(('192.168.32.219', port))
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



# Connecting with A again
s = socket.socket()          
port = 2004
s.connect(('192.168.32.227', port))
# Talking to A
print('Sending confirmation to A')

nonce_B = rint(10**12, 10**18)

confirmation_to_A = str(nonce_sent_by_A) + '||' + str(nonce_B)
encrypted_confirmation_to_A = RSA.encrypt(confirmation_to_A, RSA.n, public_key_A)
s.send(encrypted_confirmation_to_A.encode())

encrypted_confirmation_from_A = s.recv(1024).decode()
decrypted_confirmation_from_A = RSA.decrypt(encrypted_confirmation_from_A, RSA.n, private_key_B)
print ('Received confirmation of A', decrypted_confirmation_from_A)

if(int(format(decrypted_confirmation_from_A)[0]) != nonce_B):
	print("Nonce sent is not equal to nonce_B")
else:
	print("Nonce sent is equal to nonce_B")
# s.send(b'Message 1 from B')
# Closing Connection with A
s.close()

