import sys

from HangMan.check_letter import check_l

try:
	with open('countries_and_capitals.txt') as f:
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

for pair in all_file:
	print(pair.split(' | '))


sys.exit()
print('Welcome in Hangman')
answer_l_w = ''
while answer_l_w != 'l' and answer_l_w != 'w':
	answer_l_w = input('Will you guess a letter or word? (l or w)')
	if answer_l_w == 'l':
		check_l()
	

	
	
	

life = 10


def print_hangman():
	life =- 1
	if life





	
