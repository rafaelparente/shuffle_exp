from fisher_yates_shuffle import fisher_yates_shuffle as fisher_yates
from sattolo_shuffle import sattolo_shuffle as sattolo
from spotify_shuffle import spotify_shuffle as spotify

class Song:
  def __init__(self, name, artist, album, pos):
    self.name = name
    self.artist = artist
    self.album = album
    self.pos = pos


x = [Song(1, "A", "a1", 0), Song(2, "A", "a2", 1), Song(3, "B", "b1", 2), Song(4, "C", "c1", 3),
     Song(5, "B", "b1", 4), Song(6, "A", "a1", 5), Song(7, "D", "d1", 6), Song(8, "A", "a1", 7),
     Song(9, "D", "d2", 8)]

print ("Original:")
for song in x:
  print(song.name, song.artist, song.album)

print ("\r\nFisher-Yates Shuffle:")
test = list(x)
fisher_yates.shuffle(test)
for song in test:
  print(song.name, song.artist, song.album)

print ("\r\nSattolo Shuffle:")
test = list(x)
sattolo.shuffle(test)
for song in test:
  print(song.name, song.artist, song.album)

print ("\r\nSpotify Shuffle:")
test = list(x)
spotify.shuffle(test, ["artist", "album"])
for song in test:
  print(song.name, song.artist, song.album)