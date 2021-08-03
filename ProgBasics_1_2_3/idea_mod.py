

def read_and_print_file(file):
	with open(file) as f:
		read_data = f.readlines()
	f.close()
	print('Your ideabank:')
	i = 1
	for line in read_data:
		print(str(i) + '. ' + line, end='')
		i += 1