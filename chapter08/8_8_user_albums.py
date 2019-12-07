#!/usr/bin/env python3


def make_album(artist, album, tracks=""):
    """Describes a music album."""
    retval = {'artist': artist, 'album': album}
    if tracks:
        retval['tracks'] = tracks
    return retval

while True:
    artist = input("\nEnter the artist's name (or enter 'q' to quit): ")
    if artist == "q":
        break
    album = input("Enter the album name (or enter 'q' to quit): ")
    if album == "q":
        break
    print(make_album(artist, album))
