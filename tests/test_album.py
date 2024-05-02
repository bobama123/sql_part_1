from lib.album import Album

"""
Album constructs with a id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Doolittle", 1989, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1


"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    album1 = Album(1, "Doolittle", 1989, 1)
    album2 = Album(1, "Doolittle", 1989, 1)
    assert album1 == album2

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    album = Album(1, "Doolittle", 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"
