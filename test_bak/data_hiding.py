class JustCounter:
    'Use __ to hide the attribute'
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
counter.count()
counter.count()
#print(counter.__secretCount)
print(counter._JustCounter__secretCount) # This is how to print hidden attributes
