import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Small Room", 10, 2)
        self.room_2 = Room("Mideum Room", 15, 5)
        self.room_3= Room("Big Room", 20, 10)
        

        self.guest_1 = Guest("Nick", 10, 20)
        self.guest_2 = Guest("John", 5, 18)
        self.guest_3 = Guest("Nick", 8, 17)

        self.song_1 = Song("La-la-la song", 1)
        self.song_2=Song("Codeclan song",2)
        self.song_3=Song("Just a song",3)


    def test_room_has_name(self):
        self.assertEqual("Small Room",self.room_1.name)

    def test_room_has_till(self):
        self.assertEqual(10,self.room_1.till) 

    def test_room_has_capacity(self):
        self.assertEqual(2,self.room_1.capacity) 

    def test_room_can_add_songs(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1,self.room_1.song_count()) 

    def test_guest_check_in_when_room_empty(self):
        self.room_1.check_in(self.guest_1)
        self.assertEqual(1,self.room_1.guest_count())

    def test_guest_check_in_when_room_has_guests(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual(2,self.room_1.guest_count())

    def test_guest_check_in_when_room_full(self):
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.assertEqual(2,self.room_1.guest_count())


    def test_guest_check_in_when_guest_None(self):
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(None)
        self.assertEqual(2,self.room_1.guest_count())

    def test_guest_check_out_when_room_has_guests(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_1)
        self.room_1.check_out(self.guest_2)
        self.assertEqual(1,self.room_1.guest_count())

    def test_empty_room(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_1)
        self.room_1.empty()
        self.assertEqual(0,self.room_1.guest_count())

        
    

        



        
        