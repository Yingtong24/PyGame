#Defining Class
class person():
    #Constructor
    def __init__(self, name, age, country):
      self.name=name
      self.age=age
      self.country=country
    def inp(self):
      self.name=input("What is your name?: ")
      self.age=input("What is your age?: ")
      self.country=input("What country are you from?: ")
    def out(self):
      print(self.name)
      print(self.age)
      print(self.country)

obj1=person("Sophia",14,"China")
obj1.out()
obj1.inp()
obj1.out()
