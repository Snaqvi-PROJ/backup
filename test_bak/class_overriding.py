class Parent:
    def exampleMethod(self):
        print("parent method")

class Child(Parent):
    def exampleMethod(self):
        print("Child method")


par = Parent()
chi = Child()

par.exampleMethod()
chi.exampleMethod()
