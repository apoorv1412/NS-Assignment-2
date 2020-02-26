import socket, RSA

private_key_A = 100015691
public_key_KDA = 199570405
public_key_B = -1
ID_A = 10


def format(msg):
	return msg.split('||')


'''
Sending request to KDA asking for public key of B
'''       
s = socket.socket()            
port = 10002           
s.connect(('192.168.32.218', port))
message = 'Connection request of B' + '||' + '.'
# message = RSA.encrypt(message, RSA.n, )
s.send(str.encode(message))
reply = s.recv(1024)
reply = reply.decode()
decrypted_reply = RSA.decrypt(reply, RSA.n, public_key_KDA)
public_key_B = int(format(decrypted_reply)[0])
print ('Got public key of B', public_key_B) 
s.close()

'''
Sending message to B, asking for confirmation
'''
port = 2002
s = socket.socket()
s.connect(('192.168.59.49', port))
print('Sending message to B')
request_to_B = str(ID_A) + '||' + '.'
encrypted_request_to_B = RSA.encrypt(request_to_B, RSA.n, public_key_B)
s.send(str.encode(encrypted_request_to_B))
s.close()

# '''
# Listening to B's response
# '''
# port = 12345 
# s = socket.socket()
# s.bind(('', port))         
# print ("socket binded to %s" %(port)) 
# s.listen()      
# print ("socket is listening")            
# c, addr = s.accept()      
# print ('Connected to B') 
# print ('received confirmation from B')
# c.send(b'Sending confirmation to B')
# message = str(c.recv(1024))
# print (message)
# c.close()
