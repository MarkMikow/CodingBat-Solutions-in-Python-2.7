'''
Return True if the given string contains an appearance 
of "xyz" where the xyz is not directly preceeded by a 
period (.). So "xxyz" counts but "x.xyz" does not.
'''

def xyz_there(str):
  s1 = 'xyz'
  s2 = '.xyz'
  if str.find(s2) >= 0:
    str.replace(s2,'')
  new = str.replace(s2, '')
  if new.find(s1) >= 0:  
    return True
  else:
    return False