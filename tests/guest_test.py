import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Nick", 10, 20)

        
    def test_guest_has_name(self):
        self.assertEqual("Nick",self.guest.name)   

    def test_guest_has_wallet(self):
        self.assertEqual(10,self.guest.wallet)   

    def test_guest_has_age(self):
        self.assertEqual(20,self.guest.age)      