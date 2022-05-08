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


class Player:
    def __init__(self, player, fuel, status, popularity, location):
        self.owner = player
        self.fuel = fuel
        self.status = status
        self.popularity = popularity
        self.place = location

    def changeFuel(self, num):
        self.fuel += num

    def changeStatus(self, num):
        self.status += num

    def changePop(self, num):
        self.popularity += num

    def resetTime(self):
        self.time = 0

    def changePlace(self, num):
        self.place += num

    def getFuel(self):
        return self.fuel

    def getStatus(self):
        return self.status

    def getPop(self):
        return self.popularity

    def getOwner(self):
        return self.owner

    def getPlace(self):
        return self.place


compTeam = []
myPlayer = []

names = [
    "Arjun", "Ayush", "Krish", "Kieran", "Danny", "Jason", "Elon Musk",
    "Jeffery Bezos", "MONKE", "Ayoub", "Mr. Franco", "Anjan", "Ayden", "Mateen"
]


def createPlayers():
    n = random.choice(names)
    myPlayer.append(Player(n, 0, 0, random.randint(1, 50), 0))
    names.remove(n)

    for i in range(9):
        n = random.choice(names)
        compTeam.append(Player(n, 0, 0, random.randint(1, 50), 0))
        names.remove(n)

    printStats()


def printStats():

    global myPlayer
    global compTeam

    print("PLAYER TEAM")
    for i in myPlayer:
        print('''
Stats for ''' + i.getOwner() + "\n Fuel = " + str(i.getFuel()) +
              "\n Status = " + str(i.getStatus()) + "\n Popularity = " +
              str(i.getPop()) + "\n Place = " + str(i.getPlace()))

    print('''
        
COMPUTER TEAM''')
    for i in compTeam:
        print('''
Stats for ''' + i.getOwner() + "\n Fuel = " + str(i.getFuel()) +
              "\n Status = " + str(i.getStatus()) + "\n Popularity = " +
              str(i.getPop()) + "\n Place = " + str(i.getPlace()))


def runRace():
    global myPlayer
    global temparray

    myPlayer[0].resetTime()
    for i in range(len(compTeam)):
        compTeam[i].time = 0

    print("How many laps do you want to run?")
    inp = int(input(""))

    for g in range(inp):
        for x in myPlayer:
            temp = 40 / (math.sqrt(x.getSpeed()) + math.sqrt(x.getAero()) / 2 +
                         math.sqrt(x.getTires()) + math.sqrt(x.getHandling()) /
                         2 + math.sqrt(x.getBraking()) / 2)
            temp = round(temp, 2)
            x.changeRaceTime(temp)
            if random.randint(1, 10) == 1:
                x.changeRaceTime(round(x.getPitTime()))

        for x in compTeam:
            temp = 40 / (math.sqrt(x.getSpeed()) + math.sqrt(x.getAero()) / 2 +
                         math.sqrt(x.getTires()) + math.sqrt(x.getHandling()) /
                         2 + math.sqrt(x.getBraking()) / 2)
            temp = round(temp, 2)
            x.changeRaceTime(temp)
            if random.randint(1, 10) == 1:
                x.changeRaceTime(round(x.getPitTime()))

    printResults()


def randEvent():
    global money

    if random.randint(1, 50) == 1:
        d = random.choice(temparray)

        print(str(d.getOwner()) + " got a flat tire")
        d.changeRaceTime(random.randint(1, 10))

    if random.randint(1, 100) == 1:
        for d in temparray:

            print("The Le Mans Disaster happened")
            d.changeRaceTime(random.randint(10, 30))

    if random.randint(1, 200) == 1:
        d = random.choice(temparray)

        print(str(d.getOwner()) + " had a power failure")
        d.changeRaceTime(random.randint(10, 200))

    if random.randint(1, 200) == 1:

        print("You got surprise sponsorship for $500,000")
        money += 500000


def printResults():
    global myPlayer
    global temparray
    global mcar
    global money

    printStats()

    temparray = []

    temparray = list(compTeam)

    temparray.append(myPlayer[0])

    randEvent()

    temparray.sort(key=attrgetter('time'))

    mcar = temparray.index(myPlayer[0])

    print(mcar)

    for i in temparray:
        print('''
              

          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) +
              "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " +
              str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) +
              "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" +
              "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " +
              str(i.getAero()) + "\n Popularity = " + str(i.getPop()) +
              "\n Points = " + str(i.getPoints()) + "\n Time = " +
              str(i.getRaceTime()) + " minutes")

    print('''


          
THE WINNER IS... ''' + temparray[0].getOwner() + "!")

    print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) +
          "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " +
          str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) +
          "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" +
          "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " +
          str(i.getAero()) + "\n Popularity = " + str(i.getPop()) +
          "\n Points = " + str(i.getPoints()) + "\n Time = " +
          str(i.getRaceTime()) + " minutes")

    print(len(compTeam))

    print('''
        
        Finishers in Order:
        
        ''')

    n = 0
    for i in temparray:
        n += 1
        if mcar == n - 1:
            print('''
          ''' + str(n) + '''.  ''' + str(i.getOwner()) + " (YOU!)")
            money += n * 1000000 + i.getPop()
            i.changePop(random.randint(1000, 100000))
            print(money)
        else:
            print('''
          ''' + str(n) + '''.  ''' + str(i.getOwner()))

    improveStats()


def improveStats():

    global myPlayer
    global money

    i = 0
    for h in temparray:
        i += 1
        if i == 1:
            h.changePoints(25)
        elif i == 2:
            h.changePoints(18)
        elif i == 3:
            h.changePoints(15)
        elif i == 4:
            h.changePoints(12)
        elif i == 5:
            h.changePoints(10)
        elif i == 6:
            h.changePoints(8)
        elif i == 7:
            h.changePoints(6)
        elif i == 8:
            h.changePoints(4)
        elif i == 9:
            h.changePoints(2)
        elif i == 10:
            h.changePoints(1)
        else:
            pass

    myPlayer[0] = temparray[mcar]
    temparray.pop(mcar)

    upgrading = True

    while upgrading == True:
        if money > 10000:
            print("Money: $" + str(money))
            upgrade = int(
                input('''
  What do you want to upgrade? 1 for speed, 2 for braking, 3 for handling, 4 for pit time, 5 for tires, and 6 for aerodynamics, and 7 to not upgrade
  '''))
            if upgrade == 1:
                up = int(
                    input(
                        "How much do you want to upgrade your speed? 1 for 5 mph ($10,000), 2 for 25 mph ($500,000), 3 for 50 mph ($1,000,000)   "
                    ))
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
                up = int(
                    input(
                        "How much do you want to upgrade your braking? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "
                    ))
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
                up = int(
                    input(
                        "How much do you want to upgrade your handling? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "
                    ))
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
                up = int(
                    input(
                        "How much do you want to upgrade your pit time? 1 for 0.5 sec ($10,000), 2 for 2.5 sec ($500,000), 3 for 5 sec ($1,000,000)   "
                    ))
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
                up = int(
                    input(
                        "How much do you want to upgrade your tires? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "
                    ))
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
                up = int(
                    input(
                        "How much do you want to upgrade your aerodynamics? 1 for 5 levels ($10,000), 2 for 25 levels ($500,000), 3 for 50 levels ($1,000,000)   "
                    ))
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
        i.changeSpeed(random.randint(10, 20) / 10 * m)
        i.changeBraking(random.randint(10, 20) / 10 * m)
        i.changeHandling(random.randint(10, 20) / 10 * m)
        i.changePitTime((random.randint(5, 30) / 10 * m) / 100)
        i.changeTires((random.randint(5, 30) / 10 * m) / 100)
        i.changeAero((random.randint(5, 30) / 10 * m) / 100)

        while i.getPitTime() < 0:
            i.changePitTime(random.randint(1, 60))

        m += 1

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


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) +
              "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " +
              str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) +
              "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" +
              "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " +
              str(i.getAero()) + "\n Popularity = " + str(i.getPop()) +
              "\n Points = " + str(i.getPoints()) + "\n Time = " +
              str(i.getRaceTime()) + " minutes")

    print('''


          
THE WINNER IS... ''' + temparray[0].getOwner() + "!")

    print('''


          
Stats for ''' + i.getOwner() + "\n Player = " + str(i.getPlayerName()) +
          "\n Top Speed = " + str(i.getSpeed()) + "\n Handling = " +
          str(i.getHandling()) + "\n Braking = " + str(i.getBraking()) +
          "\n Pit Times: " + str(round(i.getPitTime() * 60, 2)) + " sec" +
          "\n Tires = " + str(i.getTires()) + "\n Aerodynamics = " +
          str(i.getAero()) + "\n Popularity = " + str(i.getPop()) +
          "\n Points = " + str(i.getPoints()) + "\n Time = " +
          str(i.getRaceTime()) + " minutes")

    print('''
        
        Placing in order:
        
        ''')
    n = 0
    for i in temparray:
        n += 1
        if mcar == n - 1:
            print('''
          ''' + str(n) + '''.  ''' + str(i.getOwner()) + " (YOU!)")
        else:
            print('''
          ''' + str(n) + '''.  ''' + str(i.getOwner()))


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


clearConsole()

numRaces = 22

main()
