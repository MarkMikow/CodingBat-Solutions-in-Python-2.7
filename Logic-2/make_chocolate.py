'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use 
big bars before small bars. Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
	small_amount = small * 1
	big_amount = big * 5
	
	if big == 0:
		if small_amount >= goal:
			return goal
		else:
			return '-1'
			
	if big > 0 and big_amount < goal:
		leftover = goal - big_amount
		if small_amount >= leftover:
			return leftover
		else:
			return -1
			
	if big > 0 and big_amount >= goal:
		for i in range(1, big + 1):
			if (i * 5) == goal:
				return 0
			if (i * 5) > goal:
				if small_amount >= goal:
					return goal
				else:
					return -1				
			if (i * 5) < goal and (i * 5) > (goal - 5):
				result = i * 5
				result_remainder = goal % result
				if small_amount >= result_remainder:
					return result_remainder
				else:
					return -1 