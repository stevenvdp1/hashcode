class Ride:
<<<<<<< Updated upstream
  def __init__(self,r_id, x_s,y_s,x_e,y_e, t_s, t_e):
    self.ride_id = int(r_id)
    self.x_start = int(x_s)
    self.y_start = int(y_s)
    self.x_end = int(x_e)
    self.y_end = int(y_e)
    self.start_t = int(t_s)
    self.end_t = int(t_e)
    self.ride_length = abs(self.x_start-self.x_end)+abs(self.y_start-self.y_end)

class Car:
  def distanceToStart(self, ride):
    return abs(self.x-ride.x_start)+abs(self.y-ride.y_start)
  
  def findRide(self, rides):
    pass

  def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.rideIdArray = []
        self.distance_travelled = 0




f = open("input/a_example.in", "r")
# f = open("input/b_should_be_easy.in", "r")
# f = open("input/c_no_hurry.in", "r")
# f = open("input/d_metropolis.in", "r")
# f = open("input/e_high_bonus.in", "r")

g = f.readline().split()

row = int(g[0])
col = int(g[1])
veh = int(g[2])
rid = int(g[3])
bon = int(g[4])
ste = int(g[5])

def initRides():
  rides = []
  for x in range(rid):
    ride = f.readline().split()
    rides.append(Ride(x, ride[0],ride[1],ride[2],ride[3],ride[4],ride[5]))
  return rides

def initCars():
  cars = []
  for x in range(veh):
    cars.append(Car(0,0))
  return cars

def main():
  rides = initRides()
  cars = initCars()


if __name__ == "__main__":
  main()
=======

    def __init__(self,i,xs,ys,xe,ye,ts,te):
        self.ride_id = int(i)
        self.x_start = int(xs)
        self.y_start = int(ys)
        self.x_end = int(xe)
        self.y_end = int(ye)
        self.start_t = int(ts)
        self.end_t = int(te)
        self.length = abs(self.x_start-self.x_end)+abs(self.y_start-self.y_end)

class Car:
    completedRides = []
    
    def __init__(self, a, b):
        self.x = int(a)
        self.y = int(b)



f = open("a_example.in", "r")
# f = open("b_should_be_easy.in", "r")
# f = open("c_no_hurry.in", "r")
# f = open("d_metropolis.in", "r")
# f = open("e_high_bonus.in", "r")

g = f.readline().split()

R = int(g[0])
C = int(g[1])
F = int(g[2])
N = int(g[3])
B = int(g[4])
T = int(g[5])

cars = []
rides = []

for x in range(F):
    cars.append(Car(0,0))

for x in range(N):
    ride = f.readline().split()
    rides.append(Ride(x, ride[0],ride[1],ride[2],ride[3],ride[4],ride[5])) 

>>>>>>> Stashed changes
