import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Nick", 10, 20)
        self.guest_1 = Guest("Nick", 30, 20)
        self.guest_2 =Guest("Mary",10,25)
        
        self.room_1 = Room("Small Room", 10, 2)
        self.room_2 = Room("Mideum Room", 15, 5)
        self.room_3= Room("Big Room", 20, 10)
        

        
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

