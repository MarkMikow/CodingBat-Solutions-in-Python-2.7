'''
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. You may assume 
that the array is length 3 or more.
'''

def centered_average(nums):
	a = min(nums)
	nums.remove(a)
	
	b = max(nums)
	nums.remove(b)
	
	return sum(nums) / len(nums)
	

