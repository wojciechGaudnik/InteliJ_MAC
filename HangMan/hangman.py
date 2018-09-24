alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = 'WIELKA DUPA JAS SALATA'
long = len(word)

dashed_word = ''
for chr in word:
	if chr != ' ':
		dashed_word += '_'
	else:
		dashed_word += ' '

print(word)
print(dashed_word)



b = '$'
while b:
	b = input("leter:").capitalize()
	alphabet = list(alphabet)
	if b in alphabet:
		while b in word:
			word = list(word)
			dashed_word = list(dashed_word)
			num = word.index(b)
			dashed_word[num] = b
			word[num] = '*'
		alphabet.remove(b)
		word = ''.join(word)
		dashed_word = ''.join(dashed_word)
		alphabet = ''.join(alphabet)
		print(word)
		print(dashed_word)
		print(alphabet)
	else:
		print('Kill')


