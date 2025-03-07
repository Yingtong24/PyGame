class dogs:
    def __init__(self, food_brand, colour, size, breed):
        self.food_brand=food_brand
        self.colour=colour
        self.size=size
        self.breed=breed
    
    def inp(self):
        self.food_brand=input("What is the animal's food brand?: ")
        self.colour=input("What is the colour of your animal?: ")
        self.size=input("What is the size of your animal?: ")
        self.breed=input("What breed is your animal?: ")
    
    def out(self):
        print(self.food_brand)
        print(self.colour)
        print(self.size)
        print(self.breed)

obj=dogs("Purina", "Beige", "Small", "Cavamalt")
obj.out()
obj.inp()
obj.out()