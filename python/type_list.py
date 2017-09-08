def typeList(listy):

  newStringy = ''
  sum = 0

  for i in listy:
    if isinstance(i, str):
      newStringy += i + ' '
    if isinstance(i, int) or isinstance(i, float):
      sum += i

  if sum > 0 and newStringy == '':
    print('The array you entered is of integer type')
    print('Sum: {}'.format(sum))
  elif sum > 0 and newStringy != '':
    print('The array you entered is of mixed type')
    print('String: {}'.format(newStringy))
    print('Sum: {}'.format(sum))
  elif sum == 0 and newStringy != '':
    print('The array you entered is of string type')
    print('String: {}'.format(newStringy))

typeList(['magical unicorns',19,'hello',98.98,'world'])
typeList([1, 2, 3, 4])
typeList(['hello', 'world', 'coding', 'dojo'])