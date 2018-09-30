#!/usr/bin/python3.6

import sys

a = 0.0
while (type(a) is int) or (type(a) is float):
	try:
		a = int(input('Enter a number (or a letter to exit):'))
		o = input('Enter an operation:')
		b = int(input('Enter another number:'))
		if o == '+':
			print('Result:', a + b)
		elif o == '-':
			print('Result:', a - b)
		elif o == '*':
			print('Result:', a * b)
		elif o == '/':
			print('Result:', a / b)
		else:
			sys.exit()
	except ValueError:
		#sys.exit()
		pass
	except ZeroDivisionError:
		print('I give up, dividing by zero ?!')
	except:
		print(sys.exc_info())