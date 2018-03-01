class Car:
    def addRide(self, i):
        self.ritten.append(i.ride_id) 
        self.x = i.x_end
        self.y = i.y_end

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.ritten = []

class Ride:
    def __init__(self,r_id, x_s,y_s,x_e,y_e, t_s, t_e):
        self.ride_id = int(r_id)
        self.x_start = int(x_s)
        self.y_start = int(y_s)
        self.x_end = int(x_e)
        self.y_end = int(y_e)
        self.start_t = int(t_s)
        self.end_t = int(t_e)
        self.ride_length = abs(self.x_start-self.x_end)+abs(self.y_start-self.y_end)


f = open("b_should_be_easy.in", "r")
# f = open("c_no_hurry.in", "r")
# f = open("d_metropolis.in", "r")
# f = open("e_high_bonus.in", "r")

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

for x in range(veh):
    cars[x].addRide(rides[0])
    del rides[0]

outp = open("output_d.in", "w")
for x in range(veh):
    outp.write("1 "+str(cars[x].ritten[0])+"\n")
outp.close()


