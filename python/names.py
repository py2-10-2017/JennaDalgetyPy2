# def names():

#   students = [
#     {"first_name": "Michael", "last_name": "Jordan"},
#     {"first_name": "John", "last_name": "Rosales"},
#     {"first_name": "Mark", "last_name": "Guillen"},
#     {"first_name": "KB", "last_name": "Tonel"}
#   ]

#   for name in students:
#     print name["first_name"], name["last_name"]

# names()



def name_count():

  users = {
    'Students': [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Rosales'},
      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
      {'first_name' : 'Michael', 'last_name' : 'Choi'},
      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
  }

  for key, value in users.iteritems():
    for index, name in enumerate(value, 1):
      print index, " - ", name["first_name"], name["last_name"], " - ", len(name["first_name"] + name["last_name"])


name_count()