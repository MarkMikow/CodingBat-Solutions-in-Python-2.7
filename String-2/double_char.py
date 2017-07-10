'''
Given a string, return a string where for every char in the original, there are two chars.
'''

def double_char(str):
  new_str = ''
  for i in range(len(str)):
    new_str += str[i] * 2
  return new_str