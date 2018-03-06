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

class Car:
  def distanceToStart(self, ride):
    return abs(self.x-ride.x_start)+abs(self.y-ride.y_start)

  def getAvailableRides(self, rides):
    availableRides = []
    for r in range(len(rides)):
      ride = rides[r]
      if(self.distance_travelled+ self.distanceToStart(ride)+ride.ride_length<=ride.end_t):
        availableRides.append(ride)
    return availableRides

  def getAmountNextRides(self, ride, totalRides):
    for r in range(len(totalRides)):
      pass

  def findRide(self, totalRides):
    score = self.distance_travelled+self.bonus
    totalRides = self.getAvailableRides(totalRides)
    bestRideID = None
    numberOfNextRides = 0
    for r in range(len(totalRides)):
      ride = totalRides[r]
      otherRides = totalRides
      for o in range(len(otherRides)):
        if(ride.ride_id == otherRides[o].ride_id):
          del otherRides[o]
          break
      # self.getAmountNextRides(ride, otherRides)

      # if(self.getAmountNextRides(ride, totalRides)):

      # if(distance_travelled+distanceToStart <= ride.start_t)
      #   self.bonus = self.bonus + bon

  def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.rideIdArray = []
        self.distance_travelled = 0
        self.bonus = 0




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
  for c in range(len(cars)):
    print("Car: " +str(c))
    cars[c].findRide(rides)
    print("\n")


if __name__ == "__main__":
  main()