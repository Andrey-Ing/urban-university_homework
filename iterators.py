class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.variable = self.start
        if self.variable % 2:
            self.variable -= 1
        else:
            self.variable -= 2
        return self

    def __next__(self):
        self.variable += 2
        if self.variable > self.end:
            raise StopIteration
        return self.variable


even = EvenNumbers(3, 23)
print(list(even))
print(list(even))

even = EvenNumbers()
print(list(even))

en = EvenNumbers(10, 25)
for i in en:
    print(i)
