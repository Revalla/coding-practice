class Grandfather:
    def house(self):
        print("Grandfather has a house")
class Father(Grandfather):
    def bike(self):
        print("Father has a bike")
class Child(Father):
    def laptop(self):
        print("Child has a laptop")
c = Child()
c.house()
c.bike()
c.laptop()
