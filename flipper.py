""" Code Jam Qualification Round 2017. Oversized Pancake Flipper

Problem
Last year, the Infinite House of Pancakes introduced a new kind of pancake. 
It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. 
As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper
that flips exactly K consecutive pancakes. 
That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; 
it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders
on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip 
some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen.
You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, 
so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave
all pancakes happy side up, or state that there is no way to do it.

Input
The first line of the input gives the number of test cases, T. T test cases follow. 
Each consists of one line with a string S and an integer K. 
S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) 
or - (which represents a pancake that is initially blank side up).

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, 
or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
Small dataset (Test Set 1 - Visible)
2 ≤ length of S ≤ 10.
Large dataset (Test Set 2 - Hidden)
2 ≤ length of S ≤ 1000.
Sample

Input
 
3
---+-++- 3
+++++ 4
-+-+- 4

Output
  
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
  
In Case #1, you can get all the pancakes happy side up by first flipping the leftmost 3 pancakes, 
getting to ++++-++-, then the rightmost 3, getting to ++++---+, and finally the 3 pancakes that remain blank side up. 
There are other ways to do it with 3 flips or more, but none with fewer than 3 flips.

In Case #2, all of the pancakes are already happy side up, so there is no need to flip any of them.

In Case #3, there is no way to make the second and third pancakes from the left have the same side up, 
because any flip flips them both. Therefore, there is no way to make all of the pancakes happy side up.
"""
from random import random

class Flipper(object):

	def __init__(self, flipper_size, cakes_raw):
		self.cakes_raw = list(cakes_raw)
		self.flipper_size = flipper_size

	def _string_to_num(self, cakes_raw):
		numerical = []
		for cake in cakes_raw:
			if cake == '+':
				numerical.append(2)
			elif cake == '-':
				numerical.append(random())
		return numerical

	def _flip_by_one(self, raw):
		flipped_raw = []
		for n in raw:
			if n == 2:
				n = random()
			elif n != 2:
				n = 2
			flipped_raw.append(n)
		return flipped_raw

	def flip(self):
		numerical_raw = self._string_to_num(self.cakes_raw)
		cakes_raw_copy = numerical_raw[:]
		counter = 0
		reverse_crop = []
		while True:
			crop = []
			for n in cakes_raw_copy:
				if n != 2:
					if cakes_raw_copy < reverse_crop:
						return 'IMPOSSIBLE'
					n_index = cakes_raw_copy.index(n)
					crop = cakes_raw_copy[n_index:n_index + self.flipper_size]
					cakes_raw_copy = cakes_raw_copy[n_index:]
					break
			if not crop:
				return counter
			elif len(cakes_raw_copy) < self.flipper_size:
				return 'IMPOSSIBLE'
			reverse_crop = self._flip_by_one(crop)
			cakes_raw_copy = reverse_crop + cakes_raw_copy[len(reverse_crop):]
			counter += 1

T = int(input())
case_number = 0
print(' ')
for i in range(T):
	case_number += 1
	test_cases = input()
	input_string = [x for x in test_cases.split(' ')]
	flip = Flipper(int(input_string[1]), input_string[0])
	print('Case #', case_number, ': ', flip.flip(), sep = '')