import decimal


# def my_function(a):
# 	b = a - 2
# 	return b
#
# c = 3
#
# if c > 2:
# 	d = my_function(5)
# 	print(d)


# def convert_Fahrenheit_to_Celsius(Fahrenheit):
# 	return (5/9) * float(Fahrenheit-32)
#
# try:
# 	T_f = (float(input('Give the temperature in Fahrenheit:')))
# 	print(f'Temperature in Celsius: {convert_Fahrenheit_to_Celsius(T_f):3.4}')
# except:
# 	print('Something goes wrong')
import math


# Convert "8.8" to a float.
# Convert 8.8 to an integer (with rounding).
# Convert "8.8" to an integer (with rounding).
# Convert 8.8 to a string.
# Convert 8 to a string.
# Convert 8 to a float.
# Convert 8 to a boolean.

a=[]
a.append(float("8.8"))
a.append(math.ceil(8.8))
a.append(math.floor(float("8.8")))
a.append(f"{8.8:d03.4}")# % 8.8)
a.append("%d" % 8)
a.append(float(8))
a.append(bool(8))




for i in a:
	print(type(i), ' ', i)
	




