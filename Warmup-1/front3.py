def front3(str):
  if len(str) < 3:
    return str + str + str
  else:
    front = str[0:3]
    return front + front + front