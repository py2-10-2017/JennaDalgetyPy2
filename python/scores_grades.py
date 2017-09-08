import random


def scores_grades():

  print("Scores and Grades")

  for i in range(1, 11):
    grade = random.randint(60, 100)
    if 60 <= grade <= 69:
      print("Score: {}; Your grade is D".format(grade))
    if 70 <= grade <= 79:
      print("Score: {}; Your grade is C".format(grade))
    if 80 <= grade <= 89:
      print("Score: {}; Your grade is B".format(grade))
    if 90 <= grade <= 100:
      print("Score: {}; Your grade is A".format(grade))

  print("End of the program. Bye!")

scores_grades()