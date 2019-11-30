#!/usr/bin/env python3

guests = ['bjork', 'veronica', 'ghandi']
non_guest = guests.pop(1)
print(non_guest.title() + " can't make it to the party because she's in"
      + " California.  :(")
print("I would like to invite you, " + guests[0].title() + ", to my party.")
print("I would like to invite you, " + guests[1].title() + ", to my party.")
print("I found a new table!  It's even bigger!")
guests.insert(1, "michael jordan")
guests.insert(2, "foo")
guests.append("bar")
print(guests)
for guest in guests:
    print("I would like to invite you, " + guest.title() + ", to my"
          + " dinner party.")

print("Actually, I can only invite two of you because my table won't be here"
      + " in time.")
print("I'm sorry, " + guests.pop().title() + ", but I have to rescind your"
      + " invitation.")
print("I'm sorry, " + guests.pop().title() + ", but I have to rescind your"
      + " invitation.")
print("I'm sorry, " + guests.pop().title() + ", but I have to rescind your"
      + " invitation.")
print("Welcome, " + guests[0].title() + ", to the party.")
print("Welcome, " + guests[1].title() + ", to the party.")
del guests[0]
del guests[0]
print(guests)
