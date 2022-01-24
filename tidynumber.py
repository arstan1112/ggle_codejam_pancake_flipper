""" Code Jam Qualification Round 2017. Tidy Numbers

Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, 
her pencils are sorted from shortest to longest and her computers from oldest to newest. 

One day, when practicing her counting skills, she noticed that some integers, 
when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. 
Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. 
Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input
The first line of the input gives the number of test cases, T. T lines follow. 
Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output
For each test case, output one line containing Case #x: y, 
where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
Small dataset (Test Set 1 - Visible)
1 ≤ N ≤ 1000.
Large dataset (Test Set 2 - Hidden)
1 ≤ N ≤ 1018.

Sample

Input

4
132
1000
7
111111111111111110

Output

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

"""

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