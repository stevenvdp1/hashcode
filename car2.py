class Ride:
  def __init__(self,i,xs,ys,xe,ye,ts,te):
      self.ride_id = int(i)
      self.x_start = int(xs)
      self.y_start = int(ys)
      self.x_end = int(xe)
      self.y_end = int(ye)
      self.start_t = int(ts)
      self.end_t = int(te)
      self.length = abs(self.x_start-self.x_end)+abs(self.y_start-self.y_end)
      self.available = True

class Car:
  def findRideWithBonus(self, rides, T):
    bestRideTime = T
    bestRideID = None
    for r in range(len(rides)):
      ride = rides[r]
      if(ride.available):
        if(self.timeSpent + self.lengtToStart(ride)<=ride.start_t):
          rideTime = ride.start_t+ride.length
        # else:
        #   rideTime = self.timeSpent + self.lengtToStart(ride)+ride.length
          if(rideTime<=ride.end_t and rideTime<bestRideTime):
            bestRideID = ride.ride_id
            bestRideTime = rideTime
    if(bestRideID != None):
      self.x = rides[bestRideID].x_end
      self.y = rides[bestRideID].y_end
      self.timeSpent = bestRideTime
    return bestRideID

  def findRideWithoutBonus(self, rides, T):
    bestRideTime = T
    bestRideID = None
    for r in range(len(rides)):
      ride = rides[r]
      if(ride.available):
        if(self.timeSpent + self.lengtToStart(ride)<=ride.start_t):
          rideTime = ride.start_t+ride.length
        else:
          rideTime = self.timeSpent + self.lengtToStart(ride)+ride.length
        if(rideTime<=ride.end_t and rideTime<bestRideTime):
          bestRideID = ride.ride_id
          bestRideTime = rideTime
    if(bestRideID != None):
      self.x = rides[bestRideID].x_end
      self.y = rides[bestRideID].y_end
      self.timeSpent = bestRideTime
    return bestRideID

  def lengtToStart(self, ride):
    return abs(self.x-ride.x_start)+abs(self.y-ride.y_start)

  def __init__(self, a, b):
      self.x = int(a)
      self.y = int(b)
      self.timeSpent = 0
      self.completedRides = []
      self.isFinished = False


# f = open("input/a_example.in", "r")
# f = open("input/b_should_be_easy.in", "r")
# f = open("input/c_no_hurry.in", "r")
f = open("input/d_metropolis.in", "r")
# f = open("input/e_high_bonus.in", "r")

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

for c in range(F):
  print(c)
  bestRide = cars[c].findRideWithBonus(rides, T)
  if(bestRide != None):
    rides[bestRide].available = False
    cars[c].completedRides.append(bestRide)

for c in range(F):
  print(c)
  while(True):
    bestRide = cars[c].findRideWithBonus(rides, T)
    if(bestRide != None):
      rides[bestRide].available = False
      cars[c].completedRides.append(bestRide)
    else:
      break

for c in range(F):
  print(c)
  while(True):
    bestRide = cars[c].findRideWithoutBonus(rides, T)
    if(bestRide != None):
      rides[bestRide].available = False
      cars[c].completedRides.append(bestRide)
    else:
      break

# outp = open("output/output_a.in", "w")
# outp = open("output/output_b.in", "w")
# outp = open("output/output_c.in", "w")
outp = open("output/output_d.in", "w")
# outp = open("output/output_e.in", "w")

for c in range(F):
    outp.write(str(len(cars[c].completedRides)))
    for r in range(len(cars[c].completedRides)):
        outp.write(" "+str(cars[c].completedRides[r]))
    outp.write("\n")
outp.close()