class Guest:
    def __init__(self,name,wallet,age):
        self.name=name
        self.wallet=wallet
        self.age=age
        self.favorite_songs=[]


    def pay_entrance_fee(self,room_price):
        if self.wallet>=room_price: 
            self.wallet-=room_price
            return True
        else:
            return False  

    def check_favorite_song(self, room):
        common_songs = set(room.songs).intersection(self.favorite_songs)
        if len(common_songs)!=0:
            return "Whooo!"
        else:
            return "Oh noooo("    
             
