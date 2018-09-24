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

word = list(word)
dashed_word = list(dashed_word)

b = '*'
while b:
	b = 'a'  # input("leter:")
	while b in word:
		num = word.index(b)
		dashed_word[num] = b
		word[num] = '*'
	b = ''

# print(type(word))
word = string.join(word, '')
print(word)
print(dashed_word)

# b = '*'
# while b:
# 	b = 'a' #input("leter:")
# 	while b in word:
# 		num = word.index(b)
# 		dashed_word = list(dashed_word)
# 		word = list(word)
# 		word[num] = '*'
# 		word = str(word)
# 		dashed_word[num] = b
# 		# word = word.replace(b, '*')
# 		# dashed_word = dashed_word.
# 	# b = ''
# 	# sys.exit()
# print(word)
# print(dashed_word)


