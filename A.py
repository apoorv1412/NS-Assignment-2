import socket, RSA
import datetime
from random import randint as rint

port_1 = 10007
port_2 = 2007

private_key_A = 100015691
public_key_KDA = 199570405
public_key_B = -1
ID_A = 10
nonce = -1


def format(msg):
	return msg.split('||')


'''
Sending request to KDA asking for public key of B
'''       
s = socket.socket()
port = port_1  
s.connect(('127.0.0.1', port))
time_now = datetime.datetime.now()
message = 'Connection request of B' + '||' + str(time_now)
print(message)
# message = RSA.encrypt(message, RSA.n, )
s.send(str.encode(message))
reply = s.recv(1024)
reply = reply.decode()
decrypted_reply = RSA.decrypt(reply, RSA.n, public_key_KDA)
decrypted_reply = format(decrypted_reply)
print(decrypted_reply)
public_key_B = int(decrypted_reply[0])
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

print ('Got public key of B', public_key_B) 
s.close()

'''
Sending message to B, asking for confirmation
'''
port = port_2
s = socket.socket()
s.connect(('127.0.0.1', port))
print('Sending message to B')

nonce = rint(10**12, 10**18)

request_to_B = str(ID_A) + '||' + str(nonce)
encrypted_request_to_B = RSA.encrypt(request_to_B, RSA.n, public_key_B)
s.send(str.encode(encrypted_request_to_B))
s.close()

'''
Listening to B's response
'''
port = port_2
s = socket.socket()
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
s.listen()      
print ("socket is listening")            
c, addr = s.accept()      
print ('Connected to B') 
print ('received confirmation from B')
# c.send(b'Sending confirmation to B')
confirmation_from_B = c.recv(1024).decode()
decrypted_confirmation_from_B = RSA.decrypt(confirmation_from_B, RSA.n, private_key_A)
decrypted_confirmation_from_B = format(decrypted_confirmation_from_B)

if(int(decrypted_confirmation_from_B[0]) != nonce):
	print("N1 not equal")
else:
	print("N1 = nonce sent")

nonce_2 = decrypted_confirmation_from_B[1]
print ('nonce_2', nonce_2)

encrypted_confirmation_to_B = RSA.encrypt(nonce_2, RSA.n, public_key_B)
c.send(str.encode(encrypted_confirmation_to_B))

############### VERIFIED CONNECTION ESTABLISHED WITH B ##################

raw_message = 'Hi '

for _ in range(3):
	message = raw_message + str(_ + 1)
	encrypted_message = RSA.encrypt(message, RSA.n, public_key_B)
	c.send(str.encode(encrypted_message))

	confirmation_from_B = c.recv(1024).decode()
	decrypted_confirmation_from_B = RSA.decrypt(confirmation_from_B, RSA.n, private_key_A)

	desired_confirmation = "Got-it " + str(_ + 1)

	if(desired_confirmation == decrypted_confirmation_from_B):
		print("OK",message,desired_confirmation)
	else:
		print(desired_confirmation, 'not equal to', decrypted_confirmation_from_B)


c.close()
s.close()
