class Father:
    def money(self):
        print("Father has money")
class Mother:
    def care(self):
        print("Mother takes care")
class Child(Father, Mother):
    def play(self):
        print("Child is playing")
c = Child()
c.money()
c.care()
c.play()
