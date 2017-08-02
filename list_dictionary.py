# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains
# keys and the second values. Assume the lists will be of equal length.
# Your first function will take in two lists containing some strings. Here are two example lists:
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  new_dict = {}
  i = 0
  while i < len(arr1):
      new_dict[arr1[i]] = arr2[i]
      i += 1
  return new_dict
# print make_dict(name, favorite_animal)

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used
# for the keys, the shorter for the values.
names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animals = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "Bunny"]
def make_dict2(arr1, arr2):
  new_dict = {}
  keys = arr1
  values = arr2
  if len(arr2) > len(arr1):
      keys = arr2
      values = arr1

  i = 0
  while i < len(keys):
      if i > len(values)-1:
          new_dict[keys[i]] = ""
      else:
          new_dict[keys[i]] = values[i]
      i += 1
  return new_dict
print make_dict2(names, favorite_animals)
