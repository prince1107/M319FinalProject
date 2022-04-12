import random
import math
import os
from operator import attrgetter


temparray = []

money = 0


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

  
#When creating a class, it can be done either in the same .py file that it is used or as a separate file.
#If it is a separate file you would have to link them by using an import statement.
class Player:

# The init def is standard to all classes.  It is used to create all of the variables that you will use in your class
# Notice there are no globals.  They are not necessary in a class.  The word self is used throughout the class
# to indicate that the variable is available everywhere.  You may still use local variables in a method without
# the word self

# The parameters in the init def are the ones that will be used when you create an object.  Typically these are things
# that may be different in each object.  If there is a variable that always starts at a single value, then it is simply
# set to that value in the init def
# add points tires, aerodynamics, popularity for money
    def __init__(self, player, fuel, rocketStatus, popularity, location):
    # These variables are set using the parameter.  They may have the same name as the parameter, but that is not
    # necessary.
        self.owner = owner
        self.carName = carname
        self.speed = speed
        self.handling = handling
        self.braking = braking
        self.pitTime = pittime
        self.points = points
        self.popularity = popularity
        self.tires = tires
        self.aerodynamics = aerodynamics
        self.place = location

      
  # this def will keep track of the time spent on each lap by the car.  Time represents the total cumulative time in the race.
    def changeRaceTime(self,num):
      self.time+=num

    def changePoints(self,num):
      self.points+=num

    def changePop(self,num):
      self.popularity+=num
  
  #******************************************
  # create a def that will reset the time back to zero
    def resetTime(self):
      self.time = 0
  
  # The next few defs allow the statistics of the cards to be changed
    def changeSpeed(self,num):
      self.speed+=num
  
  #******************************************
  # create 2 more defs.  One will change the handling and one will change the braking

    def changeBraking(self, m):
        self.braking += m

    def changeTires(self, m):
        self.tires += m
      
    def changeAero(self, m):
        self.aerodynamics += m

    def changeHandling(self, m):
        self.handling += m

    def changePitTime(self, m):
        self.pitTime += m
  
  # The next few defs simply return the contents of a variable.  This is necessary so that the code that uses the
  # object will be able to access the data within the object.  Returns are the only way to get information out
  # of a class.  These defs are simple, but it is possible to put more code than a simple return into them.
    def getRaceTime(self):
      return self.time
      
    def getPoints(self):
      return self.points

    def getPop(self):
      return self.popularity
  
  #******************************************
  # create the rest of the defs you will need to return information
            
    def getOwner(self):
        return self.owner

    def getHandling(self):
        return self.handling
    
    def getPlayerName(self):
        return self.carName

    def getTires(self):
        return self.tires
      
    def getAero(self):
        return self.aerodynamics

    def getSpeed(self):
        return self.speed

    def getBraking(self):
        return self.braking
    
    def getPitTime(self):
      return self.pitTime

    
    #****************************************************
    #Create the rest of the variables needed here

    # owner, carname, speed, handling, braking, pittime, points, tires, aerodynamics, popularity, time
      
    #*****************************************
    #Create a variable called time that will be set to zero







# Starting at this point is the actual program that will run.  We are out of the class.

# cars represents the array of Player objects
compTeam = []
# myPlayer is a single Player object
myPlayer= []
# carnames contains strings that are chosen at random later
#******************************************
#create an array called carnames that will have strings representing the types of cars that will race such as Porsche
names = ["Arjun", "Hamilton", "Russell", "Verstappen", "Perez", "Leclerc", "Sainz", "Norris", "Ricciardo", "Alonso", "Ocon", "Gasly", "Tsunoda", "Vettel", "Stroll", "Bottas", "Zhou", "Latifi", "Albon", "Mazepin", "Schumacher", "Ayush", "Krish", "Kieran", "Danny", "Jason"]


carnames = ["Lamborghini Countach", "Ferrari F40", "Porsche 918 Spyder", "Lamborghini Murcielago", "Porsche Carrera GT", "Mercedes Benz SLS AMG Black Series", "Bugatti Chiron", "Bugatti Veyron", "Lamborghini Aventador SVJ", "Lamborghini Veneno", "Lexus LFA", "McLaren Senna", "Dodge Viper ACR", "Saleen S7", "Ferrari F50", "Pagani Huayra BC", "Pagani Zonda", "Lamborghini Huracan Performante", "Mercedes Benz SLR McLaren", "Ferrari Scuderia Spider 16M", "McLaren 675 LT", "Chevrolet Corvette C7 ZR1", "Ferrari 599 GTO", "Ferrari Enzo", "Aston Martin V12 Vanquish S", "Lamborghini Gallardo Superleggera", "Koenigsegg Jesko", "Ariel Atom", "Detomaso Pantera", "Mclaren 720S Spider", "Bentley Continental GT3-R", "Jaguar XJ220", "Acura NSX", "Porsche 911 RUF CTR Yellowbird", "Porsche 959", "Hennessey Venom GT", "Mclaren F1", "Ferrari F12tdf", "Audi R8 V10 Plus", "Porsche 911 GT2 RS", "Ferrari 488 Pista", "Koenigsegg The One:1", "Aston Martin One-77", "Mercedes-Benz CLK-GTR", "McLaren Speedtail", "Apollo IE", "Mars Rover Concept"]


# This def will create all of the Player objects with the initialized variables.  It is important to think through
# the Player class before doing this method so that it won't be necessary to redo it later.
# Generally you would only run this method once at the beginning of your project.  However there may be times you wish
# to add new cars to the array or remove some of the ones that are already there from the array.

#  self, owner, carname, speed, handling, braking, pittime, points, tires, aerodynamics, popularity, time

def createPlayers():
  n = random.choice(names)
  myPlayer.append(Player(n, random.choice(carnames), random.randint(28, 300), random.randint(1, 50), random.randint(1, 50), random.randint(10, 100)/100, 0, random.randint(1,50), random.randint(1,50), random.randint(100,1000), 0))
  names.remove(n)
  for i in range(9):
    n = random.choice(names)
    compTeam.append(Player(n, random.choice(carnames), random.randint(28, 300), random.randint(1, 50), random.randint(1, 50), random.randint(10, 100)/100, 0, random.randint(1,50), random.randint(1,50), random.randint(100,1000), 0))
    names.remove(n)

  # ******************************************
  #The first step is to initialize my Player


  # Second we initialize all of the computer cars that will be raced against
  # ******************************************

  #Once the Players are initialised, we need a method that will print the data so we can see what has happened
  printStats()

# This def simply prints the data in a nice way.  There is no right way to do it.
def printStats():
  #First we print myPlayer's data
  # ******************************************
  global myPlayer
  global compTeam


  # Second we print all of the computers cars data
  # ******************************************

#  self, owner, carname, speed, handling, braking, pittime, points, tires, aerodynamics, popularity, time
  
  print("PLAYER TEAM")
  for i in myPlayer:
    print('''
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")

  print('''
        
COMPUTER TEAM''')
  for i in compTeam:
    print('''
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")

# This def actually runs the race
def runRace():
  #Step 1 is to reset all of the times in the objects back to zero.  This is necessary if you plan on running more
  # than 1 race
  global myPlayer
  global temparray
  # ******************************************
  
  myPlayer[0].resetTime()
  for i in range(len(compTeam)):
    compTeam[i].time = 0

  
  # We can now ask how many laps that want to be run.  This isn't necessary but adds some interest.
  print("How many laps do you want to run?")
  inp = int(input(""))
  
  # The next loop run the race for however many laps you have chosen.
  # The equation that you use to run the race is arbitrary at this point.  The goal would be to use the attributes
  # that you have chosen for your cars in and equation such that the end result makes sense.
  
  # ******************************************

  for g in range(inp):
    for x in myPlayer:
      temp = 40 / (math.sqrt(x.getSpeed()) + math.sqrt(x.getAero()) / 2 + math.sqrt(x.getTires()) + math.sqrt(x.getHandling()) / 2 + math.sqrt(x.getBraking()) / 2)
      temp = round(temp,2)
      x.changeRaceTime(temp)
      if random.randint(1,10) == 1:
        x.changeRaceTime(round(x.getPitTime()))
        
    
    for x in compTeam:
      temp = 40 / (math.sqrt(x.getSpeed()) + math.sqrt(x.getAero()) / 2 + math.sqrt(x.getTires()) + math.sqrt(x.getHandling()) / 2 + math.sqrt(x.getBraking()) / 2)
      temp = round(temp,2)
      x.changeRaceTime(temp)
      if random.randint(1,10) == 1:
        x.changeRaceTime(round(x.getPitTime()))
    # equation to calculate the time for the race
    # ******************************************


  printResults()
    # calling the changeRaceTime def in the class allows you to pass the variable you used in the equation into
    # your object to change the variable called time.
    # ******************************************

    #  This loop will do the same for the computer cars
    # ******************************************


# This is another method you could use to make the simulation more interesting.  You may choose to make some random
# events that have a chance of occuring during any lap of the race, before the race, or after the race.  These events
# may affect the attributes of the car temporarily (like a flat) or permanently.
def randEvent():
  if random.randint(1,50) == 1:
    d = random.choice(temparray)

    print(str(d.getOwner()) + " got a flat tire")
    d.changeRaceTime(random.randint(1,10))

  if random.randint(1,100) == 1:
    for d in temparray:

      print("The Le Mans Disaster happened")
      d.changeRaceTime(random.randint(10,30))

  if random.randint(1,200) == 1:
    d = random.choice(temparray)

    print(str(d.getOwner()) + " had a power failure")
    d.changeRaceTime(random.randint(10,200))

  if random.randint(1,200) == 1:
    
    print("You got surprise sponsorship for $500,000")
    money += 500000

#This def is used to print the results after the race is over.
def printResults():
  #The first step is to print the accumulated times of each car during the race.
  global myPlayer
  global temparray
  global mcar
  global money

  printStats()
  # ******************************************
 
  temparray = []

  temparray = list(compTeam)

  temparray.append(myPlayer[0])

  randEvent()
  
  temparray.sort(key=attrgetter('time'))

  mcar = temparray.index(myPlayer[0])
  
  print(mcar)

  for i in temparray:
    print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")

  # The second step is to find out who actually won and print the winners name.

  # ******************************************
  print('''


          
THE WINNER IS... ''' + temparray[0].getOwner() + "!")

  print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")
  
  print(len(compTeam))
# This def is used to improve the stats of the cars after the race.  The code should fit some criteria you have
# established.  For instance you may choose to only improve the stats of the winners or you may choose to make the
# players buy upgrades with some amount of money they have won.
  print('''
        
        Finishers in Order:
        
        ''')

  n = 0
  for i in temparray:
    n += 1
    if mcar == n-1:
      print( '''
          ''' + str(n) + '''.  ''' + str(i.getOwner()) + " (YOU!)")
      money += n * 1000000 + i.getPop()
      i.changePop(random.randint(1000,100000))
      print(money)
    else:
      print( '''
          ''' + str(n) + '''.  ''' + str(i.getOwner()))

  
  improveStats()
  
def improveStats():
  # First step is improve the stats of the computer cars
  global myPlayer
  global money

  i = 0
  for h in temparray:
    i += 1
    if i==1:
      h.changePoints(25)
    elif i==2:
      h.changePoints(18)
    elif i==3:
      h.changePoints(15)
    elif i==4:
      h.changePoints(12)
    elif i==5:
      h.changePoints(10)
    elif i==6:
      h.changePoints(8)
    elif i==7:
      h.changePoints(6)
    elif i==8:
      h.changePoints(4)
    elif i==9:
      h.changePoints(2)
    elif i==10:
      h.changePoints(1)
    else:
      pass
  
  # ******************************************

  myPlayer[0] = temparray[mcar]
  temparray.pop(mcar)

  upgrading = True

  while upgrading == True:
    if money > 10000:
      print("Money: $" + str(money))
      upgrade = int(input('''
  What do you want to upgrade? 1 for speed, 2 for braking, 3 for handling, 4 for pit time, 5 for tires, and 6 for aerodynamics, and 7 to not upgrade
  '''))
      if upgrade == 1:
        up = int(input("How much do you want to upgrade your speed? 1 for 5 mph ($10,000), 2 for 25 mph ($500,000), 3 for 50 mph ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changeSpeed(5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changeSpeed(25)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changeSpeed(50)
            money -= 1000000
      if upgrade == 2:
        up = int(input("How much do you want to upgrade your braking? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changeBraking(5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changeBraking(25)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changeBraking(50)
            money -= 1000000
      if upgrade == 3:
        up = int(input("How much do you want to upgrade your handling? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changeHandling(5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changeHandling(25)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changeHandling(50)
            money -= 1000000
      if upgrade == 4:
        up = int(input("How much do you want to upgrade your pit time? 1 for 0.5 sec ($10,000), 2 for 2.5 sec ($500,000), 3 for 5 sec ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changePitTime(-0.5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changePitTime(-2.5)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changePitTime(-5)
            money -= 1000000
      if upgrade == 5:
        up = int(input("How much do you want to upgrade your tires? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changeTires(5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changeTires(25)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changeTires(50)
            money -= 1000000
      if upgrade == 6:
        up = int(input("How much do you want to upgrade your aerodynamics? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "))
        if money > 10000:
          if up == 1:
            myPlayer[0].changeAero(5)
            money -= 10000
        if money > 500000:
          if up == 2:
            myPlayer[0].changeAero(25)
            money -= 500000
        if money > 1000000:
          if up == 3:
            myPlayer[0].changeAero(50)
            money -= 1000000
      if upgrade == 7:
        upgrading = False
    else:
      upgrading = False

  
      
  m = 1
  for i in temparray:
    i.changeSpeed(random.randint(10,20)/10 * m)
    i.changeBraking(random.randint(10,20)/10 * m)
    i.changeHandling(random.randint(10,20)/10 * m)
    i.changePitTime((random.randint(5,30)/10 * m)/100)
    i.changeTires((random.randint(5,30)/10 * m)/100)
    i.changeAero((random.randint(5,30)/10 * m)/100)
    
    while i.getPitTime() < 0:
      i.changePitTime(random.randint(1,60))
    
    m += 1
    
    
  #Second step is to improve the stats of my car.
  # ******************************************

  compTeam = list(temparray)
  print(len(compTeam))


def end():
  temparray = []

  temparray = list(compTeam)

  temparray.append(myPlayer[0])

  randEvent()
  
  temparray.sort(key=attrgetter('points'))

  mcar = temparray.index(myPlayer[0])
  
  print(mcar)

  for i in temparray:
    print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")

  # The second step is to find out who actually won and print the winners name.

  # ******************************************
  print('''


          
THE WINNER IS... ''' + temparray[0].getOwner() + "!")

  print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) + "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " + str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) + "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" + "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " + str(i.getAero()) + "\n Popularity = " + str(i.getPop()) + "\n Points = " + str(i.getPoints()) + "\n Time = " + str(i.getRaceTime()) + " minutes")

  print('''
        
        Placing in order:
        
        ''')
  n = 0
  for i in temparray:
    n += 1
    if mcar == n-1:
      print( '''
          ''' + str(n) + '''.  ''' + str(i.getOwner()) + " (YOU!)")
    else:
      print( '''
          ''' + str(n) + '''.  ''' + str(i.getOwner()))

  
#This method runs the entire project

def main():
  global numRaces
  
  raceAgain = True
  createPlayers()
  while raceAgain:
    runRace()

    numRaces -= 1
    
    if numRaces > 0:
      printStats()
      raceAgain = True
    else:
      raceAgain = False
# ******************************************
clearConsole()

numRaces = 22

main()

