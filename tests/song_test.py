import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("La-la-la", 1)
        
    def test_song_has_name(self):
        self.assertEqual("La-la-la",self.song.name)

    def test_song_has_price(self):
        self.assertEqual(1,self.song.price)          
        
        