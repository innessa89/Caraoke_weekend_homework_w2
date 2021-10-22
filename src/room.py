class Room:
    def __init__(self,name,till,capacity):
        self.name=name
        self.till=till
        self.capacity=capacity
        self.songs=[]
        self.guest=[]

  
    def add_song(self,song):
        return self.songs.append(song)

    def song_count(self):
        return len(self.songs)

    def check_in(self,guests):
        if self.capacity>len(self.guest):
            return self.guest.append(guests)
        else:
            return "The room is full! Please, wait!"   
            
    def guest_count(self):
        return len(self.guest) 

    def check_out(self,guest):
        return self.guest.remove(guest)

    def empty(self):
        return self.guest.clear()  