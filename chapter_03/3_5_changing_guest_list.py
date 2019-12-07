#!/usr/bin/env python3

# 3-5 Changing Guest List: you just heard that one of your guests can't make
# the dinner, so you need to send out anew set of invitations.  You'll have to
# think of someone else to invite.
# - Start with your program from Exercise 3-4.  Add a print statement at the end
#   of your program stating the name of the guest who can't make it.
# - Modify your list, replacing the name of the guest who can't make it with
#   the name of the new person you are inviting.
# - Print a second set of invitation messages, one for each person who is still
#   in your list.

guests = ['bjork', 'veronica', 'ghandi']
non_guest = guests.pop(1)
print(non_guest.title() + " can't make it to the party because she's in California.  :(")
print("I would like to invite you, " + guests[0].title() + ", to my party.")
print("I would like to invite you, " + guests[1].title() + ", to my party.")
