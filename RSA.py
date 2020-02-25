block_size = 31


def encrypt(message, n, e):
	binary_string = ''
	for a in message:
		b = bin(ord(a))[2:]
		b = '0'*(8-len(b)) + b
		binary_string += b
	rem = len(binary_string) % block_size
	binary_string += '1'
	binary_string += (block_size-rem-1)*'0'

	print ('encrypted binary_string', binary_string)
	print ('len of binary', len(binary_string))
	
	encrypted_string = ''

	num_blocks = len(binary_string) // block_size
	for i in range(num_blocks):
		curr = binary_string[i * block_size : (i + 1) * block_size]
		print ('len of curr', len(curr))
		curr = int(curr,2)
		# print ('before',curr)
		curr = pow(curr,e,n)
		# print ('after',curr)
		curr = bin(curr)[2:]
		print ('len of curr', len(curr))
		curr = '0' * (block_size - len(curr)) + curr
		encrypted_string += curr

	print ('encrypted_string', encrypted_string)
	return encrypted_string

def decrypt(message, n, d):
	binary_string = ''
	num_blocks = len(message) // block_size
	for i in range(num_blocks):
		curr = message[i * block_size : (i + 1) * block_size]
		curr = int(curr,2)
		curr = pow(curr,d,n)
		curr = bin(curr)[2:]
		curr = '0' * (block_size - len(curr)) + curr
		binary_string += curr

	print ('decrypted binary_string', binary_string)

	binary_string = binary_string.rstrip('0')
	binary_string = binary_string[:len(binary_string) - 1]
	
	decrypted_string = ''
	num_chars = len(binary_string) // 8

	for i in range(num_chars):
		curr = binary_string[i * 8 : (i + 1) * 8]
		curr = int(curr,2)
		decrypted_string += chr(curr)

	print ('decrypted string -', decrypted_string, '-')
	print ('len ', len(decrypted_string))
	return decrypted_string



p = 45293
q = 45389
phi = (p-1)*(q-1)
print (phi)
n = p*q
e = 1001629
d = 199570405

message = "wtf chinmay hyderabad kon jata hai???!!!!"
# print (ord(message))

encrypted_string = encrypt(message, n, e)
# print (encrypted_string)
decrypted_string = decrypt(encrypted_string, n, d)
# print (decrypted_string)
print (len(decrypted_string))
# print (ord(chr(decrypted_string)))
