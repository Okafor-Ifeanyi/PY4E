class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, 'Constructed')

    def party(self):
        self.x += 1
        print(f"{self.name} Party count {self.x}")

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(f"{self.name} points {self.points} ")

s = PartyAnimal('Kizito')
s.party()

j = FootballFan("BIO")
# j.party()
# j.party()
# j.party()
# j.touchdown()
# j.touchdown()
