
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


