import array
import string

a = [i for i in string.ascii_uppercase]

b = [ord(i) + 1 for i in a if ord(i) > 2]
print([chr(a) for a in b])
print(a)

a = b
b[0] = "jaś"
print(a)

del a[0]
print(a)
c = a.copy()
print(c)
c[0] = 'asdfasdf'
print(a)
print(c)
c.pop(0)
print(c)

a = 1
b = '1'

if a is b:
	print("the same")

if a == b:
	print('asdf')
	
print(c)
# c.append('a')
print(sum(c))
print(all(c))
print(c.count(70))
c.extend(['adf', 'asdf', 'asdddd'])
print(c)
print(c.index('adf'))
c.insert(0, 'aaaaaaaaa')
print(c)
b = c.pop(-1)
print(b)
print(c)

numbers = [3, 2, 4, 1]
print(sorted(numbers))
print(numbers)
# numbers = sorted(numbers)
# print(numbers)
print(list(reversed(numbers)), 'asdf')
numbers = list(reversed(numbers))
print(numbers)

numbers = [3, 2, 4, 1]

# these return a modified copy, which we can print
print(numbers, '<---')
print(sorted(numbers))
print(list(reversed(numbers)), 'TODO <---nie odwraca dlaczego ????') # TODO <---nie odwraca dlaczego ????

# the original list is unmodified
print(numbers)

# now we can modify it in place
# numbers.sort()
# numbers.reverse()
#
# print(numbers)
print([1, 2, 3] + [4, 5])
print([1, 2, 3] * 2)
print('aaa')

# b = array('l') # TODO <--- wyłącza print
print(a, '<--a')
print('a')
print(numbers, '<---')


a = [1, 2, 3, 4]
b = a
print(a)
b[0] = 999
print(a)