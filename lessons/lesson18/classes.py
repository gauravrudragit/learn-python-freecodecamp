class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print(f"{self.make} Moves.....")

    def get_make_model(self):
        print(f"I am a {self.make} {self.model}")


my_car = Vehicle("Ford", "mustang")
my_car.get_make_model()
my_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print(f"{self.make} Flies")


class Truck(Vehicle):
    def moves(self):
        print(f"{self.make} Rumbles")


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', "1233")
mack = Truck('Cat', 'dumpster')
cart = GolfCart('yamaha', 'mc10')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
cart.get_make_model()
cart.moves()

print("\n\n\n")

for v in (my_car, cessna, mack, cart):
    v.get_make_model()
    v.moves()
