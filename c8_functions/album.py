def make_album(artist_name, album_title, song_nember=None):
    """A dictionary that include music album's informations."""
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if song_nember:
        album["number of songs"] = song_nember
    return album


album1 = make_album("ali sorena", "gavazn", 18)
album2 = make_album("bahram", "khodha", 12)
album3 = make_album("shayea", "amade bash")
print(f"\n{album1}")
print(f"\n{album2}")
print(f"\n{album3}")
