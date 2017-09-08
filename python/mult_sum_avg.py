def odds():

  for i in range(1, 1000):
    if i % 2 != 0:
      print i

odds()



def fives():

  for i in range(5, 1000000):
    if i % 5 == 0:
      print i

fives()



def sums():

  sum = 0
  a = [1, 2, 5, 19, 255, 3]

  for i in a:
    sum += i

  print sum

sums()



def avgs():

  sum = 0

  a = [1, 2, 5, 19, 255, 3]

  for i in a:
    sum += i

  avg = sum / len(a)

  print avg

avgs()