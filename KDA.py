# first of all import the socket library 
import socket, RSA
import datetime

port_1 = 10007
port_2 = 2007

def format(msg):
	return msg.split('||')

private_key_KDA = 1001629
public_key_A = 1893307107
public_key_B = 1841622505
  
s = socket.socket()          
print ("Socket successfully created")
  
port = port_1
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
s.listen()      
print ("socket is listening")            
  
# Establish connection with A. 
c, addr = s.accept()      
print ('Connected to A')  	
request = c.recv(1024).decode()
request = format(request)
formatted_request = request[0]
print (formatted_request)
time_in_request = date_time_obj = datetime.datetime.strptime(request[1], '%Y-%m-%d %H:%M:%S.%f')

if(abs((time_in_request - datetime.datetime.now()).total_seconds()) > 1):
	print("INVALID MESSAGE")
else:
	print("MESSAGE RECEIVED WITHIN TIME")

print ('Sending public key of B')
message = str(public_key_B) + '||' + request[0] + '||' + str(datetime.datetime.now())
print('Sending this', message)
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
