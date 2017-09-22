def list_to_dict():

  name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
  favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

  spirit_animal = zip(name, favorite_animal)
  animal_dict = dict(spirit_animal)

  print animal_dict

list_to_dict()


# def list_to_dict(name, favorite_animal):

#     spirit_animal = dict(zip(name, favorite_animal))

#     print spirit_animal

# list_to_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])