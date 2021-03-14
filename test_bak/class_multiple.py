class First:
    def __init__(self):
        print("First cons")

    def testfunc1(self):
        print("test func 1")

class Second:
    def __init__(self):
        print("Second cons")

    def testfunc2(self):
        print("test func 2")

class Third(Second):
    def __init__(self):
        print("Third cons")


obj3 = Third()
dir(obj3)


