# def is_triangle(a, b, c):
# 	mylist = []
# 	mylist.append(a)
# 	mylist.append(b)
# 	mylist.append(c)
# 	for i in mylist:
# 		if i <= 0:
# 			return False
# 	if (mylist[0] + mylist[1] > mylist[2]) and mylist[0] + mylist[2] > mylist[1] and mylist[1] + mylist[2] > mylist[0]:
# 		return True
# 	return False
#
#
# user_names = []
# def validate(username, password):
# 	a = 'Wrong username or password!' if ((('||' or '//') in password) or (username in user_names)) else 'Successfully Logged in!'
# 	user_names.append(username)
# 	return a
#
#
# print(validate('Timmy','password'))
# print(validate('Timmy','h4x0r'))
# print(validate('Alice','alice'))
# print(validate('Timmy','password"||""=="'))
# print(validate('Admin','gs5bw"||1==1//'))


# def shortest_arrang(n):
# 	lista = []
# 	ii = -1
# 	i = 0 if n % 2 == 1 else 1
# 	while sum(lista) != n:
# 		ii += 1
# 		lista = []
# 		while sum(lista) != n:
# 			lista.append((n // 2) - i - ii + (n % 2))
# 			if sum(lista) < n:
# 				i += 1
# 				if 0 in lista:
# 					return [-1]
# 				continue
# 			i = 1
# 			break
# 		pass
# 	return lista
#
# 	# print(a)
# 	# while sum(lista) != n:
# print(shortest_arrang(65))#,[33, 32]))
# print(shortest_arrang(10))#,[4, 3, 2, 1]))
# print(shortest_arrang(14))#,[5, 4, 3, 2]))
# print(shortest_arrang(22))#,[7, 6, 5, 4]))
# print(shortest_arrang(16))#,[-1]))

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return ( (blue_start-blue_pulled)) / ((blue_start-blue_pulled) + (red_start-red_pulled))


print(guess_blue(5, 5, 2, 3)) #, 0.6)
print(guess_blue(5, 7, 4, 3)) #, 0.2)
print(guess_blue(12, 18, 4, 6)) #, 0.4)

