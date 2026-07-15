class Employee:
    def work(self):
        print("Employee is working")
class Manager(Employee):
    def work(self):
        print("Manager is managing the team")
e = Employee()
m = Manager()
e.work()
m.work()
