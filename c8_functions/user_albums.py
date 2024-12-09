def make_album(artist_name, album_title, song_nember=None):
    """A dictionary that include music album's informations."""
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if song_nember:
        album["number of songs"] = song_nember
    return album


print("\nFor getting your result, fill following asks:")
print("(enter 'q' whenever you want to exit): ")

while True:
    album = input("\nAlbum's name: ")
    if album == "q":
        break
    
    artist = input("\nArtist's name: ")
    if artist == "q":
        break

    output = make_album(artist, album)
    print(f"{output}\n")
