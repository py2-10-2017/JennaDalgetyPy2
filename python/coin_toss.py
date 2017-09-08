import random

def coin_toss():

  attempt = 0
  heads = 0
  tails = 0

  print("Starting the program...")

  for i in range(1, 5001):
    coin = random.randint(1, 2)
    if coin == 1:
      attempt += 1
      heads += 1
      print("Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(attempt, heads, tails))
    if coin == 2:
      attempt += 1
      tails += 1
      print("Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(attempt, heads, tails))

  print("Ending the program, thank you!")

coin_toss()