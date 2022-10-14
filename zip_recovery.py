import zipfile
import itertools
import multiprocessing as mp
import time
import sys
import hashlib

input_file_name = 'file.zip'
extensive_input_charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._*+,!?/:'
input_charset = 'abcdefghijklmnopqrstuvwxyz'

#####################################################################################

def unzip(password):


	try:
		
		wrong_password = False
		with zipfile.ZipFile(input_file_name) as file:
	
			file.extractall(pwd = bytes(password, 'utf-8'))
						
	except:
		
		wrong_password = True
		return 'wrong password'
	
	finally:
		
		# Will only be executed if their is no error thrown
		if not wrong_password:	
			#print('correct password')
			return 'correct password'

	
#####################################################################################

# Need to add the option of multithreading as well as running the code on the GPU
	
def crack_zip(start = 1, end = 2, file_name = input_file_name, charset = input_charset):
	
	total_iterations = sum([len(charset)**x for x in range(end + 1)])
	count = 1
	
	for iteration in range(start, end + 1):
		
		temp_permutations = itertools.product(charset, repeat = iteration)
		
		for p in temp_permutations:
			
			current_password = ''.join(p)
			
			result = unzip(current_password)
			print(current_password + ' - ' + result + ' - ' + str(count) + ' of ' + str(total_iterations) + ' - {}%'.format(round(count / total_iterations, 2)))
			
			count += 1
			if result == 'correct password':
				return current_password

#crack_zip(1,3)

