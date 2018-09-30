# Triangle area ----------------------------------------------------
# numbers = [0, 0, 0, 3, 5, 0]
# numbers = [0, 0, 2, 2, 4, 0]
# import sys
#
# try:
# 	numbers = input(
# 		'Give mi six integers a, b, c, d, e, f - the coordinates \n'
# 		'of the vertices of the triangle '
# 		'(a, b), (c, d) and (e, f):')
# 	if ',' in numbers:
# 		numbers = numbers.split(',')
# 		numbers = [int(i) for i in numbers]
# 	else:
# 		numbers = numbers.split()
# 		# numbers = list(map(int, numbers))
# 		numbers = [int(i) for i in numbers]
# 	if len(numbers) > 6:
# 		raise NameError('Too many numbers')
# 	for i in numbers:
# 		if abs(i) > 100:
# 			raise NameError('Out of range -100 to 100')
# except ValueError:
# 	sys.exit('You have to give mi numbers')
# except NameError as name:
# 	sys.exit(name)
# except Exception as exception:
# 	print(exception.__class__)
#
# x1 = numbers[0]
# y1 = numbers[1]
# x2 = numbers[2]
# y2 = numbers[3]
# x3 = numbers[4]
# y3 = numbers[5]
#
# triangle_field = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
# print(triangle_field)

# Roman numbers ----------------------------------------------------
import sys


def int_to_roman(n):
        string=''
        symbol=['M','D','C','L','X','V','I']
        value = [1000,500,100,50,10,5,1]
        num = 10 ** (len(str(n)) - 1)
        quo = n // num
        rem = n % num
        if quo in [0,1,2,3]:
            string = string + symbol[value.index(num)] * quo
        elif quo in [4,5,6,7,8]:
            tem_str = symbol[value.index(num)] + symbol[value.index(num) - 1] + symbol[value.index(num)] * 3
            string = string + tem_str[(min(quo,5) - 4) : (max(quo,5) - 3)]
        else:
            string = string + symbol[value.index(num)] + symbol[value.index(num) - 2]
        if rem == 0:
            return string
        else:
            string = string + int_to_roman(rem)
        return string

try:
	n = int(input('Give natural number (written in Arabic numerals, greater than zero and less than 4000):'))
	if not (0 < n < 4000):
		raise NameError('Out of range')
	print(int_to_roman(n))
except NameError as name:
	sys.exit(name)
except ValueError as exception:
	sys.exit(exception)
except Exception as exception:
	print(exception.__class__)
