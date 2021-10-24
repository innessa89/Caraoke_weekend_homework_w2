import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar=Bar(
            {
            "wine":3,
            "beer":2,
            "margarita":4
        }
        )

        self.guest_1 = Guest("Nick", 30, 20)
        self.guest_2 = Guest("John", 60, 18)
        self.guest_3 = Guest("Mike", 50, 17)
        self.guest_4 =Guest("Mary",10,25)
        self.guest_5 =Guest("Ann",0,25)

    def test_bar_has_drinks(self):
        self.assertDictEqual({"wine":3,"beer":2,"margarita":4},self.bar.drinks_dictionary)  

    def test_guest_age_too_young_to_drink(self):
        orderResult=self.bar.order(self.guest_3,"wine") 
        self.assertEqual("Come back when you are 18!",orderResult)

    def test_drink_in_the_list(self):
        orderResult=self.bar.order(self.guest_1,"cola") 
        self.assertEqual("Drink is not in the menu.",orderResult)   

    def test_guest_doesnt_have_enough_money(self):
        orderResult=self.bar.order(self.guest_5,"wine") 
        self.assertEqual("Not enough money",orderResult) 

    def test_guest_make_order(self):
        orderResult=self.bar.order(self.guest_1,"wine") 
        self.assertEqual("Enjoy!",orderResult) 
        self.assertEqual(self.bar.orders_dictionary[self.guest_1].count("wine"),1)
        self.assertEqual(27,self.guest_1.wallet)
        self.assertEqual(3,self.bar.till)


