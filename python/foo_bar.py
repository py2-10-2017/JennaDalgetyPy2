def prime_square_check():

  for i in range(1, 101):
    prime = True
    squarey = False
    
    # for s in range(1, i):
    #   if (s * s == i) and (i % s == s):
    #     squarey = True

    if i**i == i * i:
      squarey = True

    for p in range(2, i):
      if (i % p == 0):
        prime = False

    if prime:
      print str(i) + " Foo"
      continue

    if squarey:
      print str(i) + " Bar"
      continue
    
    print str(i) + " FooBar"

prime_square_check()