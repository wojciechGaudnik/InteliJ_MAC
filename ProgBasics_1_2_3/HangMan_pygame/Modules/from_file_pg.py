import random, sys

def random_words(file_name):
	try:
		with open(file_name) as f:
			all_file = []
			one_line = f.readline()
			while one_line:
				all_file.append(one_line[:-1])
				one_line = f.readline()
		f.close()
	except IOError:
		print('Problem with file of words')
		sys.exit()
	except Exception as other_error:
		print(Exception.__class__)
		print(other_error)
		sys.exit()
	
	all_words = []
	for pair in all_file:
		all_words.append(pair.split(' | '))
	return(random.choice(all_words))
