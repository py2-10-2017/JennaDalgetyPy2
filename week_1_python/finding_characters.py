def finder(listy, char):

  results = []

  for i in listy:
    if char in i:
      results.append(i)

  print results

finder(['hello', 'world', 'my', 'name', 'is', 'Anna'], 'm')