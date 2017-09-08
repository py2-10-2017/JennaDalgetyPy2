# def draw_stars(listy):

#   for i in listy:
#     print "*" * i

# draw_stars([4, 6, 1, 3, 5, 7, 25])


def draw_stars(listy):

  for i in listy:
    if isinstance(i, int):
      print("*" * i)
    if isinstance(i, str):
      print i.lower()[0] * len(i)

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])