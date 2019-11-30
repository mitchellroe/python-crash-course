#!/usr/bin/env python3

# From 4_2_animals.py
animals = ['bear', 'lion', 'human', 'jaguar', 'cheetah', 'giraffe',
           'rhinoceros']
for animal in animals:
    print(animal.capitalize() + "s are very frightening animals.")

print("All of these animals do some pretty nasty things to other animals,"
      + " but one of them doesn't do it for survival, whereas the other two"
      + " do.")

print("The first three items in the list are: " + str(animals[:3]))
mean = int((len(animals) / 2) - 1)
print("The mean index is: " + str(mean))
print("Three items from the middle of the list are: "
      + str(animals[mean - 1:mean + 2]))
print("The last three items in the list are: " + str(animals[-3:]))
