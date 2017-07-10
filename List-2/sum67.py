'''
Return the sum of the numbers in the array, except ignore 
sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.
'''

def sum67(nums):
	nums = nums[:]
	while 6 in nums:
		i = nums.index(6)	# finds the index of the first element that 
							# has a value of 6
		j = nums.index(7,i)	# finds the index of the first element that 
							# has a value of 7 after the index i
		del nums[i:j+1]		# deletes elements in range from i -> j
	return sum(nums)