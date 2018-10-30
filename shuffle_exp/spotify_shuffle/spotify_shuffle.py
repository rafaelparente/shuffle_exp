import random

def fisher_yates_shuffle(x):
  for i in range(len(x)-1, 0, -1):
    j = random.randrange(i + 1)
    x[i], x[j] = x[j], x[i]

def shuffle(x, y):
  songs_by_y = {}
  
  for song in x:
    y_attrib = getattr(song, y[0])
    if y_attrib not in songs_by_y:
      songs_by_y[y_attrib] = list()
    songs_by_y[y_attrib].append(song)

  for songs in songs_by_y.values():
    song_count = len(songs)
    appear_base = 100/song_count
    appear_lim = appear_base - 100/(song_count+1)
    appear_max, appear_min = appear_base + appear_lim, appear_base - appear_lim
    
    offset_lim = 100.0 - (appear_max * (song_count - 1))
    offset = random.uniform(0, offset_lim)

    if len(y) > 1:
      shuffle(songs, y[1:])

    fisher_yates_shuffle(songs)

    songs[0].pos = offset
    
    for i in range (1, song_count):
      songs[i].pos = songs[i-1].pos + random.uniform(appear_min, appear_max)

  x.sort(key=lambda i: i.pos)