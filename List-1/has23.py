'''
Given an int array length 2, return True if it contains a 2 or a 3.
'''

def has23(nums):
  if nums[0] != 2 and nums[0] != 3 and nums[1] != 2 and  nums[1] != 3:
    return False
  return True
      
