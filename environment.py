

from artist import Artist
from genre import Genre
from song import Song


lady_gaga = Artist("Lady Gaga")
lcd_soundsystem = Artist("LCD Soundsystem")
vulfpeck = Artist("Vulfpeck")


pop = Genre("Pop")
rock = Genre("Rock")
alt = Genre("Alternative")
indie = Genre("Indie")
folk = Genre("Folk")
country = Genre("Country")
funk = Genre("Funk")
jam = Genre("Jam")
# create as many genres as you'd like

song_1 = Song("Poker Face", lady_gaga, pop)
song_1b = Song("gaga b", lady_gaga, funk)
song_2 = Song("lcd song", lcd_soundsystem, alt)
song_2b = Song("lcd b", lcd_soundsystem, country)
song_3 = Song("vulv song", vulfpeck, rock)
song_3b = Song("vulv b", vulfpeck, jam)



