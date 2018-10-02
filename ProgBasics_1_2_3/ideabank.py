import sys
from idea_mod import read_and_print_file

if '--list' in sys.argv:
	read_and_print_file('ideas.txt')
elif '--delete' in sys.argv:
	read_data = []
	num_del = 0
	try:
		num_del = int(sys.argv[2]) - 1
		f = open('ideas.txt', 'r')
		read_data = f.readlines()
		f.close()
		read_data.__delitem__(num_del)
		f = open('ideas.txt', 'w')
		for line in read_data:
			f.write(line)
		f.close()
		read_and_print_file('ideas.txt')
	except:
		print('Number out of list or file doesn\'t exists, or file is empty')
else:
	answer = ''
	while not answer:
		try:
			answer = input('What is your new idea:')
		except:
			print('Repeat')
	try:
		f = open('ideas.txt', 'a')
	except:
		f = open('ideas.txt', 'w')
	f.write(answer + '\n')
	f.close()
	read_and_print_file('ideas.txt')

