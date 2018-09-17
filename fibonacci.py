

j = 1
k = 0
fib = 0
fib_tab = []
spaces = "{:10d}"
fib_str_max = ""

print('Fibonacci sequance:')
i = int(input('How many numbers would you like to calculate:'))

for n in range(1, i + 1):
	fib_tab.insert(n, fib)
	fib = j + k
	j = k
	k = fib

fib_str_max = len(str(fib_tab[-1]))
i = 1
for f in fib_tab:
	spaces = str('{:' + str(fib_str_max + len(str(len(fib_tab))) - len(str(i))) + '}')
	print(str(i) +': ' + spaces.format(f))
	i += 1
