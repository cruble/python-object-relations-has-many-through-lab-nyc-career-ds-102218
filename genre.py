# remeber to import the Song class here
from song import Song

class Genre:

	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name): 
		self._name = name 

	def songs(self):
		songs = []
		for song in Song.all(): 
			if song.genre == self:
				songs.append(song)
		return songs 

	def artists(self):
		return list(set(map(lambda song: song.artist, self.songs())))


