import sys
from setC_mod import sort
numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]


try:
	numbers = input(
		'Give me numbers to sort, you can be separated by comma or space'
		' and afterwards press enter:')
	if ',' in numbers:
		numbers = numbers.split(',')
		# numbers = list(map(int, numbers))
		numbers = [int(i) for i in numbers]
	else:
		numbers = numbers.split()
		# numbers = list(map(int, numbers))
		numbers = [int(i) for i in numbers]
except ValueError:
	# print('You have to give mi numbers')
	sys.exit('You have to give mi numbers')
except Exception as exception:
	print(exception.__class__)


print(numbers)
sort(numbers)
print(numbers)






