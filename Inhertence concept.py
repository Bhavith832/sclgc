class Plane:
    def land(self):
        print("plane is landing")
    def takeoff(self):
        print("plane had takoff")

class Passenger(Plane):
    def carry_passenger(self):
        print("plane is carring passenger")

class Cargo(Plane):
    def carry_goods(self):
        print("plane is carrying goods")

class Fighter(Plane):
    def carry_weapons(self):
        print("plane is carrying weapons")

p=Passenger()
p.land()
p.takeoff()
p.carry_passenger()

c=Cargo()
c.land()
c.takeoff()
c.carry_goods()

f=Fighter()
f.land()
f.takeoff()
f.carry_weapons()

