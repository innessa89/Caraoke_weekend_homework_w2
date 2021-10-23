class Room:
    def __init__(self,name,price,capacity):
        self.name=name
        self.price=price
        self.capacity=capacity
        self.songs=[]
        self.guests=[]
        self.till=0

  
    def add_song(self,song):
        return self.songs.append(song)

    def song_count(self):
        return len(self.songs)


#test_capacity_avalible_and_guest_can_pay
#test_capacity_avalible_and_guest_cant_pay
#test_capacity_not_avalible

    def check_in(self,guest): 
        if self.capacity>len(self.guests):
            if guest.pay_entrance_fee(self.price):
                self.till+=self.price
                return self.guests.append(guest)
            else:
                return "Not enough money"
        else:
            return "The room is full! Please, wait!"   
            
    def guest_count(self):
        return len(self.guests) 

    def check_out(self,guest):
        if self.guests.count(guest)!=0:
            return self.guests.remove(guest)

    def empty(self):
        return self.guests.clear()  

   

