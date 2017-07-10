def front_back(str):
  if len(str) == 0:
    return ''
  elif len(str) == 1:
    return str
  elif len(str) == 2:
    begin = str[-1]
    end = str[0]
    return begin + end
  elif len(str) > 2:
    begin = str[-1]
    middle = str[1:-1]
    end = str[0]
    return begin + middle + end