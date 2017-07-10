'''
Given an array length 1 or more of ints, return the 
difference between the largest and smallest values in the array. 
'''

def big_diff(nums):
	a = min(nums)
	b = max(nums)
	return abs(a - b)