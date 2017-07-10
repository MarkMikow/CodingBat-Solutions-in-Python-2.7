'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and 
big bricks (5 inches each). Return True if it is possible to make the 
goal by choosing from the given bricks. This is a little harder 
than it looks and can be done without any loops. 
'''

def make_bricks(small, big, goal):
  	small_amount = small * 1
	big_amount = big * 5
	
	if big == 0:
		if small_amount >= goal:
			return True
		return False
			
	elif big > 0 and big_amount < goal:
		leftover = goal - big_amount
		if small_amount >= leftover:
			return True
		return False
			
	elif big > 0 and big_amount >= goal:
		for i in range(big + 1):
			if (i * 5) <= goal and (i * 5) > (goal - 5):
				result = i * 5
				result_remainder = goal % result
				if small_amount >= result_remainder:
					return True
				return False