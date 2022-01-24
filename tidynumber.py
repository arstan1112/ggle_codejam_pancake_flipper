def check_edge_cases(number):
	if len(str(number)) == 1:
		return True
	arr = [int(i) for i in str(number)]
	first = arr[0]
	for n in arr:
		if n != first:
			return False
	return True

def get_tidy_array(number):
	arr = [int(i) for i in str(number)]
	start = 1
	digits_difference = 0
	alike_digits_counter = 0
	for ind, n in enumerate(arr):
		if n < start:
			if digits_difference >= 1:
				arr[ind - 1] = arr[ind - 1] - 1
				arr = arr[:ind] + [9 for i in arr[ind:]]
				return arr
			else:
				if ind - alike_digits_counter >= 1:
					arr[ind - alike_digits_counter - 1] = arr[ind - alike_digits_counter -1] - 1
					arr = arr[:ind - alike_digits_counter] + [9 for i in arr[ind - alike_digits_counter:]]
				else:
					arr = [9 for i in range(len(arr) - 1)]
				return arr
		elif n > start:
			alike_digits_counter = 0
			digits_difference = n - start
			start = n
		elif n == start:
			alike_digits_counter += 1
			digits_difference = 0
			start = n
			
	return arr

def get_tidy_number(number):
	if check_edge_cases(number):
		return number
	tidy_array = get_tidy_array(number)
	tidy_number = int("".join(map(str, tidy_array)))
	return tidy_number


T = int(input())
case_counter = 0
print(" ")
for n in range(T):
	case_counter += 1
	number = int(input())
	print("Case #{}: {}".format(case_counter, get_tidy_number(number)))