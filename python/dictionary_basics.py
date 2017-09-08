# def my_dictionary():

#   data = {
#     'My name is': "Jenna",
#     'My age is': 37,
#     'My country of birth is': "United States",
#     'My favorite language is': "Python"
#   }

#   for key, value in data.iteritems():
#     print key, value

# my_dictionary()



def my_dictionary():

  data = {
    'name': "Jenna",
    'age': 37,
    'country of birth': "United States",
    'language': "Python"
  }

  questions = []
  answers = []

  for key, value in data.iteritems():
    questions.append(key)
    answers.append(value)

  for q, a in zip(questions, answers):
    print("My {} is {}".format(q, a)) 

my_dictionary()


