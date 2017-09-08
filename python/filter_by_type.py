def filter():

  thingy = ['name','address','phone number','social security number']

  print thingy
  if isinstance(thingy, int) == True:
    if thingy >= 100:
      print("That's a big number")
    else:
      print("That's a small number")
  if isinstance(thingy, str) == True:
    if len(thingy) >= 50:
      print('Long sentence')
    else:
      print('Short sentence')
  if isinstance(thingy, list) == True:
    if len(thingy) >= 10:
      print('Big list')
    else:
      print('Short list')

filter()