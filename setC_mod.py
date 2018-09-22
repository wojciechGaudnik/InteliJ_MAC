def sort(numbers_list):
	N = len(numbers_list)
	interations = 1
	while interations < N:
		j = 0
		while j <= N - 2:
			if numbers_list[j] > numbers_list[j + 1]:
				numbers_list[j + 1], numbers_list[j] = numbers_list[j], numbers_list[j + 1]
			j += 1
		interations += 1