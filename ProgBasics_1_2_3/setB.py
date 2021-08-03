# Modulo --------------------------------------------
number = 0
natural = 100

while number <= 25:
	if (((natural / 7) >= 1) and ((natural % 7)) == 0) or (((natural / 9) >= 1) and ((natural % 9)) == 0):
		print(str(number) + '. ' + str(natural))
		number += 1
	natural += 1

# The greatest common divisor --------------------------------------------
a = 0;
b = 0;
while a == 0 or b == 0:
	try:
		a = int(input('a:'))
		b = int(input('b:'))
	except:
		print('again')

nwd = a if a < b else b
while (a % nwd != 0) or (b % nwd != 0):
	nwd -= 1
print(nwd)


a = 0;
b = 0;
while a == 0 or b == 0:
	try:
		a = int(input('a:'))
		b = int(input('b:'))
	except:
		print('again')

nwd = 0
while nwd == 0:
	if a < b:
		a, b = b, a
	if a - b == 0:
		nwd = a
	else:
		a = a - b
print(nwd)

# Present participle form --------------------------------------------
words = input('Give me infinite verbs:').lower().split()
consonant = 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, X, Z, W, Y'.lower().replace(' ', '').split(',')
volwel = 'A, E, I, O, U'.lower().replace(' ', '').split(',')
for word in words:
	if (len(word) > 2) and (word[-1] in consonant) and (word[-2] in volwel) and (word[-3] in consonant):
		print(word + 'ing')
	elif (len(word) > 2) and word[-2:] == 'ie':
		print(word[0:-2] + 'ying')
	elif word == 'be':
		print('being')
	elif len(word) >= 3 and word[-2:] == 'ee':
		print(word + 'ing')
	elif word[-1] == 'e':
		print(word[0:-1] + 'ing')

# Anagrams --------------------------------------------
name_file = 'anagrams.csv'
words = ''
while name_file == '' or len(words) == 0:
	try:
		name_file = input('File name:')
		with open(name_file) as f:
			words = f.read()
		f.close()
	except:
		f.close()
		print('Again')

words = words.split('\n')
words.__delitem__(-1)
words_buf = words[:]
words.sort()
words_buf.sort()

for word in words:
	if word[::-1] in words_buf:
		print(word, word[::-1])
		words_buf.remove(word)
		words_buf.remove(word[::-1])


