# EXERCISE 5
import pylast
from itertools import islice

def get_similar_tracks(artist,track):
  last = pylast.LastFMNetwork(api_key="#your_api_key", api_secret="#your_api_secret")
  track = last.get_track(artist,track)
  for similar in islice(track.get_similar(), 5):
    # limited to the first 5 similar tracks
    print similar.item

# python interpreter

# >> reload(exercise5)
# >> exercise5.get_similar_tracks('Cher','Believe')

#Response:

#<similartracks track="Believe" artist="Cher">
#  <track>
#    <name>Ray of Light</name>
#    <mbid/>
#    <match>10.95</match>
#    <url>http://www.last.fm/music/Madonna/_/Ray+of+Light</url>
#    <streamable fulltrack="0">1</streamable>
#    <artist>
#      <name>Madonna</name>
#      <mbid>79239441-bfd5-4981-a70c-55c3f15c1287</mbid>
#      <url>http://www.last.fm/music/Madonna</url>
#    </artist>
#    <image size="small">http://cdn.last.fm/coverart/50x50/1934.jpg</image>
#    <image size="medium">http://cdn.last.fm/coverart/130x130/1934.jpg</image>
#    <image size="large">http://cdn.last.fm/coverart/130x130/1934.jpg</image>
#  </track>
#  ...
#</similartracks>
