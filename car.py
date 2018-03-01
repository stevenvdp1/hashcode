class Car:
    def addRide(self, i):
        self.ritten.append(i) 

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.ritten = []

    

class Ride:
    def __init__(self,ride_id, x_start,y_start,x_end,y_end, start_t, end_t):
        self.ride_id = int(ride_id)
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.x_end = int(x_end)
        self.y_end = int(y_end)
        self.start_t = int(start_t)
        self.end_t = int(end_t)


f = open("e_high_bonus.in", "r")
g = f.readline().split()

row = int(g[0])
col = int(g[1])
veh = int(g[2])
rid = int(g[3])
bon = int(g[4])
ste = int(g[5])

cars = []
rides = []

for x in range(veh):
    cars.append(Car(0,0))

for x in range(rid):
    ride = f.readline().split()
    rides.append(Ride(x, ride[0],ride[1],ride[2],ride[3],ride[4],ride[5]))

rides = sorted(rides, key=lambda start: start.start_t)

for x in range (rid):
    print(rides[x].start_t)

for x in range(veh):
    cars[x].addRide(rides[x].ride_id)
    print(cars[x].ritten)

outp = open("output_e.in", "w")
for x in range(veh):
    outp.write("1 "+str(cars[x].ritten[0])+"\n")
outp.close()


