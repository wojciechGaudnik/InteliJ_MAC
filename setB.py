
number = 0
natural = 1

while number <= 25:
	if (((natural / 7) >= 1) and ((natural % 7)) == 0) or (((natural / 9) >= 1) and ((natural % 9)) == 0):
		print(str(number) + '. ' + str(natural))
		number += 1
	natural += 1
	
