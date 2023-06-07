class Human:
    def __init__(self):
        self.health = 100
        self.time = 10
        self.achieve = 0

    def work(self):
        self.health -= 50
        self.time -= 1
        self.achieve += 1

    def rest(self):
        self.time -= 3
        self.health += 50

class Engineer(Human):
    def work_hard(self):
        self.health -= 150
        self.time -= 3
        self.achieve += 5

soma = Engineer()
