
number_coffes = 5

class Sebastian:
    def __init__(self, n_cofee):
        self.number_coffees=n_cofee
        self.number_of_sugar_cups = 7

    def grab_coffee_pads(self, *args):
        return f'{self.number_coffees} coffee'
    
    def grab_cups(self):
        return f'{self.number_coffees} cup'
    

seb = Sebastian(5)

print(seb.grab_coffee_pads(9, 12, 13, 14,1))
print(seb.grab_cups())
