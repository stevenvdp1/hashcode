class Car:
    def addRide(self, i):
        self.ritten.append(i.ride_id)
        self.distance_travelled = self.distance_travelled + abs(self.x-i.x_start)+abs(self.y-i.y_start)
        self.x = i.x_start
        self.y = i.y_start
        if(self.distance_travelled < i.start_t):
            self.distance_travelled= i.start_t
        self.distance_travelled = self.distance_travelled + abs(self.x - i.x_end)+abs(self.y-i.y_end)
        self.x = i.x_end
        self.y = i.y_end

    def findRide(self, rides):
        posRides = []
        for x in range(len(rides)):
            if(self.distance_travelled + rides[x].ride_length + abs(self.x-rides[x].x_start)+abs(self.y-rides[x].y_start)<rides[x].end_t):
                posRides.append(rides[x])
        if(posRides):
            closest = posRides[0]
            closestdist = 1000000
            for x in range(len(posRides)):
                if(abs(self.x-posRides[x].x_start)+abs(self.y-posRides[x].y_start)<closestdist):
                    closestdist = abs(self.x-posRides[x].x_start)+abs(self.y-posRides[x].y_start)
                    closest = posRides[x]
            self.addRide(closest)
            return closest.ride_id

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.ritten = []
        self.distance_travelled = 0

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

# f = open("input/a_example.in", "r")
# f = open("input/b_should_be_easy.in", "r")
# f = open("input/c_no_hurry.in", "r")
# f = open("input/d_metropolis.in", "r")
f = open("input/e_high_bonus.in", "r")

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

rides = sorted(rides, key=lambda start: start.start_t + start.ride_length)

for x in range(veh):
    for y in range(len(rides)):
        if(abs(cars[x].x-rides[y].x_start)+abs(cars[x].y-rides[y].y_start)+rides[y].ride_length<rides[y].end_t):
            cars[x].addRide(rides[y])
            del rides[y]
            break

for x in range(len(cars)):
    d = True
    print(x)
    while d:
        r = cars[x].findRide(rides)
        print(d)
        for m in range(len(rides)):
            if(rides[m].ride_id == r):
                del rides[m]
                d=1
                break
        d = d+1
        if(d>3):
            d=False
            
# outp = open("output/output_a.in", "w")
# outp = open("output/output_b.in", "w")
# outp = open("output/output_c.in", "w")
# outp = open("output/output_d.in", "w")
outp = open("output/output_e.in", "w")
for x in range(veh):
    outp.write(str(len(cars[x].ritten)))
    for r in range(len(cars[x].ritten)):
        outp.write(" "+str(cars[x].ritten[r]))
    outp.write("\n")
outp.close()


