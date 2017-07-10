'''
Given a string, return a "rotated left 2" version where 
the first 2 chars are moved to the end. The string length 
will be at least 2.
'''

def left2(str):
  str_begin = str[2:]
  str_end = str[:2]
  return str_begin + str_end