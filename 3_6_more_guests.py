#!/usr/bin/env python3

# 3-6 You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
#
# - Start with your program from Exercise 3-4 or Exercise 3-5.  Add a print
#   statement to the end of your program informing people that you found a
#   bigger dinner table.
# - Use insert() to add one new guest to the beginning of your list.
# - Use insert() to add one new guest to the middle of your list.
# - Use append() to add one new guest to th eend of your list.
# - Print a new set of invitation messages, one for each person in your list.

guests = ['bjork', 'veronica', 'ghandi']
non_guest = guests.pop(1)
print(non_guest.title() + " can't make it to the party because she's in" +
      " California.  :(")
print("I would like to invite you, " + guests[0].title() + ", to my party.")
print("I would like to invite you, " + guests[1].title() + ", to my party.")
print("I found a new table!  It's even bigger!")
guests.insert(1, "michael jordan")
guests.insert(2, "foo")
guests.append("bar")
print(guests)
for guest in guests:
    print("I would like to invite you, " + guest.title() + ", to my" +
          " dinner party.")
