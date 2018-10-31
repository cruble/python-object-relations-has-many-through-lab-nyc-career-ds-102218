# remeber to import the Song class here
from song import Song

class Artist:

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
			if song.artist == self:
				songs.append(song)
		return songs 

	def genres(self):
		return list(set(map(lambda song: song.genre, self.songs())))
