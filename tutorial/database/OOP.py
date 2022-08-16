class PartyAnimal():
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, 'Constructed')

    def party(self):
        self.x += 1
        print(f"{self.name} Party count {self.x}")

an = PartyAnimal("Ifeanyi")
an.party()
an.party()
an.party()
an.party()

j = PartyAnimal("Naza")
j.party()
j.party()
j.party()
j.party()

