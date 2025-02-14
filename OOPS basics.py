#Defining Class
class person():
    #Constructor
    def __init__(self, name, age, country):
      self.name=name
      self.age=age
      self.country=country
      print(self.name)
      print(self.age)
      print(self.country)

obj1=person("Sophia",14,"China")