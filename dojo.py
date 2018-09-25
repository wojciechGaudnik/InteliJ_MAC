# min(), max(), sum(), sort(), sorted() etc

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44, -100, 200, [-200, "dupa2", 300]], None, 105, -43, 1.1]

def min1(lista):
	i_buf = lista[0]
	for i in lista:
		if (type(i) == int or type(i) == float) and i_buf > i:
			i_buf = i
		if type(i) == list and i_buf > min1(i):
			i_buf = min1(i)
	return(i_buf)
print(min1(numbers))


def max1(lista):
	i_buf = lista[0]
	for i in lista:
		if (type(i) == int or type(i) == float) and i_buf < i:
			i_buf = i
		if type(i) == list and i_buf < max1(i):
			i_buf = max1(i)
	return(i_buf)
print(max1(numbers))


def avr1(lista):
	i_buf = 0
	for i in lista:
		if type(i) == int or type(i) == float:
			i_buf += i
		if type(i) == list:
			i_buf += avr1(i)
	return(i_buf)

print(avr1(numbers))
