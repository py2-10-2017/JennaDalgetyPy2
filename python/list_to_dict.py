def list_to_dict():

  name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
  favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

  spirit_animal = zip(name, favorite_animal)
  animal_dict = dict(spirit_animal)

  print animal_dict

list_to_dict()