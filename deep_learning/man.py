class Man:
    def __init__(self,named):
        self.name = named
        print("Initialized!")

    def hello(self):
        print("Hello" + self.name + "!")

    def goodbye(self):
        print("Good-bye" + self.name + "!")


m = Man("David")
m.hello()
m.goodbye()
