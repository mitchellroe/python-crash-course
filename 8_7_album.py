#!/usr/bin/env python3


def make_album(artist, album, tracks=""):
    """Describes a music album."""
    retval = {'artist': artist, 'album': album}
    if tracks:
        retval['tracks'] = tracks
    return retval


print(make_album("Brand New", "Daisy"))
print(make_album("Johnny's Band", "Walking Through Hell"))
print(make_album("Nine Inch Nails", "With Teeth"))
print(make_album("Some Band", "Some Album", 17))
