import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Nick", 10, 20)
        self.guest_1 = Guest("Nick", 30, 20)
        self.guest_2 = Guest("Mary",10,25)
        
        self.room_1 = Room("Small Room", 10, 2)
        self.room_2 = Room("Mideum Room", 15, 5)
        self.room_3 = Room("Big Room", 20, 10)

        self.song_1 = Song("La-la-la song", 1)
        self.song_2 = Song("Codeclan song",2)
        self.song_3 = Song("Just a song",3)


        
    def test_guest_has_name(self):
        self.assertEqual("Nick",self.guest.name)   

    def test_guest_has_wallet(self):
        self.assertEqual(10,self.guest.wallet)   

    def test_guest_has_age(self):
        self.assertEqual(20,self.guest.age)  
    
    def test_guest_can_pay_for_room(self):
        canPay = self.guest_1.pay_entrance_fee(self.room_1.price)
        self.assertEqual(20,self.guest_1.wallet)
        self.assertEqual(True,canPay)  

    def test_guest_cant_pay_for_room(self):
        canPay = self.guest_2.pay_entrance_fee(self.room_2.price)
        self.assertEqual(10,self.guest_2.wallet)  
        self.assertEqual(False,canPay)

    def test_guest_has_favorite_song_in_room(self):
        self.room_1.songs.append(self.song_1)
        self.guest_1.favorite_songs.append(self.song_1)

        returnvalue=self.guest_1.check_favorite_song(self.room_1)

        self.assertEqual("Whooo!",returnvalue)

    def test_guest_doesnt_has_favorite_song_in_room(self):
        self.room_1.songs.append(self.song_1)
        self.guest_1.favorite_songs.append(self.song_2)
        returnvalue=self.guest_1.check_favorite_song(self.room_1)
        self.assertEqual("Oh noooo(",returnvalue)    



        

