def is_triangle(a, b, c):
	mylist = []
	mylist.append(a)
	mylist.append(b)
	mylist.append(c)
	for i in mylist:
		if i <= 0:
			return False
	if (mylist[0] + mylist[1] > mylist[2]) and mylist[0] + mylist[2] > mylist[1] and mylist[1] + mylist[2] > mylist[0]:
		return True
	return False
	