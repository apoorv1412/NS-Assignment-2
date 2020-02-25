def encrypt(message, n, e):
	encrypted_string = ''
	for a in message:
		encrypted_string += str(pow(ord(a),e,n))
		encrypted_string += ' '
	return encrypted_string

def decrypt(message, n, d):
	decrypted_string = ''
	message = message.rstrip()
	arr = list(map(int, message.split(' ')))
	for a in arr:
		decrypted_string += chr(pow(a, d, n))
	return decrypted_string


p = 449
q = 457
phi = (p-1)*(q-1)
n = p*q
e = 47
d = 59

message = 'Hello There'
encrypted_string = encrypt(message, n, e)
print (encrypted_string)
decrypted_string = decrypt(encrypted_string, n, d)
print (decrypted_string)