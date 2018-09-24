# !/usr/bin/python3.6
import sys

if len(sys.argv) > 1:
	print('Hello ' + str(sys.argv[1]) + '!')
else:
	print('Hello World  !')
	
	
	
import sys
from _cffi_backend import string

word = 'dupa jas salata'
long = len(word)

dashed_word = ''
for chr in word:
	if chr != ' ':
		dashed_word += '_'
	else:
		dashed_word += ' '

print(word)
print(dashed_word)



b = '*'
while b:
	b = input("leter:")
	while b in word:
		word = list(word)
		dashed_word = list(dashed_word)
		num = word.index(b)
		dashed_word[num] = b
		word[num] = '*'
	word = ''.join(word)
	dashed_word = ''.join(dashed_word)
	print(word)
	print(dashed_word)


