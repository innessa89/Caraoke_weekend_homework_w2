class Bar:
    def __init__(self, drinks_dictionary):
        self.drinks_dictionary=drinks_dictionary
        self.orders_dictionary={}
        self.till=0

    def order(self,guest,drink):              
# to check guests age
# check if the drink in the list of drinks
# check customer has money
# put drink to order list
        if guest.age<18:
            return "Come back when you are 18!"
        if drink not in self.drinks_dictionary:
            return "Drink is not in the menu."
        if guest.wallet<self.drinks_dictionary.get(drink):
            return "Not enough money"
        if guest not in self.orders_dictionary:
            self.orders_dictionary[guest]=[]   
        self.orders_dictionary[guest].append(drink)
        guest.wallet-=self.drinks_dictionary.get(drink)
        self.till+=self.drinks_dictionary.get(drink)
        return "Enjoy!"

   