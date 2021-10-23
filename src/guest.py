class Guest:
    def __init__(self,name,wallet,age):
        self.name=name
        self.wallet=wallet
        self.age=age


    def pay_entrance_fee(self,room_price):
        if self.wallet>=room_price: 
            self.wallet-=room_price
            return True
        else:
            return False   
        