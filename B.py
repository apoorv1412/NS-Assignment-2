# first of all import the socket library 
import socket, RSA, datetime
from random import randint as rint

port_1 = 10007
port_2 = 2007

private_key_B = 100093193
public_key_KDA = 199570405
public_key_A = -1
ID_A = -1
nonce_sent_by_A = -1
nonce_B = -1

def format(msg):
	return msg.split('||')


s = socket.socket()          
port = port_2
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
port = port_1
s = socket.socket()          
s.connect(('127.0.0.1', port))
time_now = datetime.datetime.now()
message = 'Connection request of A' + '||' + str(time_now)
# Connection request of A
s.send(str.encode(message))

reply = s.recv(1024)
reply = reply.decode()
decrypted_reply = RSA.decrypt(reply, RSA.n, public_key_KDA)
decrypted_reply = format(decrypted_reply)
print(decrypted_reply)
public_key_A = int(decrypted_reply[0])
time_from_reply = datetime.datetime.strptime(decrypted_reply[2], '%Y-%m-%d %H:%M:%S.%f')

if(abs((time_now - time_from_reply).total_seconds()) > 1):
	print("message time out")
else:
	print("message is received within time")
	# print(time_now)
	# print(time_from_reply)
if(decrypted_reply[1] != format(message)[0]):
	print("Message Corrupt")
else:
	print("Message OK")

print ('Got public key of A', public_key_A)
s.close()



# Connecting with A again
s = socket.socket()          
port = port_2
s.connect(('127.0.0.1', port))
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

############### VERIFIED CONNECTION ESTABLISHED WITH A ##################

raw_message = 'Got-it '

for _ in range(3):
	message_from_A = RSA.decrypt(s.recv(1024).decode(), RSA.n, private_key_B)
	desired_message = "Hi " + str(_ + 1)

	if(message_from_A != desired_message):
		print(message_from_A, 'not equal to', desired_message)
	else:
		print('OK', message_from_A)
		message = raw_message + str(_ + 1)
		s.send(RSA.encrypt(message, RSA.n, public_key_A).encode())

s.close()

