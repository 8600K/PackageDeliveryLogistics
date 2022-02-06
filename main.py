# Miles Engelbrecht | Student ID #001435519


import csv
from datetime import datetime
from datetime import timedelta

# No duplicate keys.
# O(1) for add, get, delete functions.

# def _get_hash(self, key):
#   hash = 0
#    for char in str(key):
#        hash += ord(char)
#    return hash % self.size
from typing import List, Set


class HashMap:
    def __init__(self):
        self.size = 32  # size
        self.map = [None] * self.size

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, v0, v1, v2, v3, v4, v5, v6):
        hashedKey = self.getHash(key)
        values = [key, v0, v1, v2, v3, v4, v5, v6]

        if self.map[hashedKey] is None:
            self.map[hashedKey] = list([values])
            return True
        else:
            for data in self.map[hashedKey]:
                if data[0] == key:
                    data[1] = v0
                    data[2] = v1  # Clean this up?
                    data[3] = v2
                    data[4] = v3
                    data[5] = v4
                    data[6] = v5
                    data[7] = v6
                    return True
            self.map[hashedKey].append(values)
            return True

    def getData(self, csvInput):
        with open(csvInput, mode='r', encoding='utf-8') as fileInput:

            csvFile = csv.reader(fileInput)

            keys = 0
            for row in csvFile:
                if row[0].isnumeric():
                    try:
                        self.add(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    except IndexError:
                        self.add(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "At Hub")
                else:
                    continue
                keys += 1
        return keys

    def get(self, key, rows):
        hashedKey = self.getHash(key)
        if self.map[hashedKey] is not None:
            for pair in self.map[hashedKey]:
                if pair[0] == key:
                    if rows == None:
                        return str(pair[0] + " " + pair[1]) + " " + str(pair[2]) + " " + str(pair[3]) + " " + str(
                            pair[4]) + " " + str \
                                   (pair[5]) + " " + str(pair[6]) + " " + str(pair[7])
                    elif rows == 0:
                        return str(pair[0])
                    elif rows == 1:
                        return str(pair[1])  # Address
                    elif rows == 2:
                        return str(pair[2])  # City
                    elif rows == 3:
                        return str(pair[3])  # State
                    elif rows == 4:
                        return str(pair[4])  # Zip
                    elif rows == 5:
                        return str(pair[5])  # Time
                    elif rows == 6:
                        return str(pair[6])  # Weight
                    elif rows == 7:
                        return str(pair[7])  # Status.  Starts blank except where a special note resides
                    else:
                        return None
        return None

    def update(self, key, row, updatedData):
        hashedKey = self.getHash(key)
        if self.map[hashedKey] is not None:
            for data in self.map[hashedKey]:
                if data[0] == key:
                    data[row] = updatedData
                    # print("This ran!  Good job.")

    def delete(self, key):
        hashedKey = self.getHash(key)
        print("Ran!")
        if self.map[hashedKey] is None:
            return False
        for i in range(0, len(self.map[hashedKey])):
            print("Ran!!!")
            if self.map[hashedKey][i][0] == key:
                self.map[hashedKey].pop(i)  # Test this with remove or some other function.
                print("RAN!!!!!")
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))


def ui():
    uInput = True
    while uInput:
        print("Do you wish to continue?  Y/N")
        uInput = input()
        print(uInput)
        if uInput.upper() == 'Y':
            continue
        elif uInput.upper() == 'N':
            print("This ran!")
            return False


def distance():
    with open("WGUPS Distance Table.csv", mode='r', encoding='utf-8') as fileInput:
        csvFile = csv.reader(fileInput)
        myList = []
        for i in csvFile:
            # print(i)
            myList.append(i)
    return myList


# ui()


distance()

h = HashMap()
keyAmount = h.getData("WGUPS Package File.csv")
# h.print()
# h.delete("31")
# h.print()

# print("Got", h.get('9'))

distList = distance()


# Turn item into what we get from the first Excel document
# item = '195 W Oakland Ave (84115)'

# Get packages that need to be delivered before EOD.
def getCertainPackages(word, index, bool=0):
    i = 1
    prime = []
    keyList = []
    while i <= keyAmount:

        if bool == 1:
            if word in h.get(str(i), 7) == 'Delivered at':
                prime.append(h.get(str(i), 1) + " (" + h.get(str(i), 4) + ")" + ":" + tempStr + " ")

        tempStr = h.get(str(i), index)
        if word in tempStr and 'Delivered at' not in h.get(str(i), 7):
            prime.append(h.get(str(i), 1) + " (" + h.get(str(i), 4) + ")" + ":" + tempStr + " ")
            # print(h.get(str(i), 0))
            # print(prime)
            keyList.append(h.get(str(i), 0))
        i += 1

    for i, primes in enumerate(prime):
        prime[i] = prime[i].split(':')[0]
    # print("Prime: ", prime)
    return prime, keyList


def printDist(sublist):
    returnList = []
    for i in distList:
        for j in sublist:
            if (j == i[1]):
                # print("FOUND!", i)
                c = len(i) - 1
                # print("Test: ", i[0:len(i)])
                if i[0:len(i)] not in returnList:  # Check this more
                    returnList.append(i[0:len(i)])
                continue
    return returnList

    # print(i [1:len(i)])


print("\n")


# GLOBAL VARIABLE FOR COUNTING


def findNxt(list, index, keyss, truckMilage, totalMiles=0, miles=0, keyCounter=0):
    print("KeysCounted", keyCounter)

    if (len(list) == 1 or keyCounter >= 16) and index != 'HUB':
        # print("This ran!  !  !")
        totalMiles += float(list[0][2])  # Gets us back to the hub.
        # print("Should be 3.7...? ", val)
        return totalMiles

    if totalMiles < miles != 0 and totalMiles != 0 and index != 'HUB':  # NOTE...
        if totalMiles + float(list[int(index)][2]) >= miles:
            totalMiles += float(list[index][2])
            # print("And here we returned... ", list[index][2])
            # print("Total Miles: ", totalMiles)
            return totalMiles
    elif totalMiles > miles != 0:
        # print("And here we returned electric 2: ", list[index][2])
        totalMiles += float(list[index][2])
        # print("Total Miles: ", totalMiles)
        return totalMiles

    newIndex = None
    val = 100.0
    test = None
    if (index == 'HUB'):
        tempTotalMiles = totalMiles
        for i, dist in enumerate(list):
            # print(dist[2])
            if float(dist[2]) < val:
                val = float(dist[2])
                totalMiles = val
                index = i
                test = dist[1][:-8]
                # print("Here it is! ",test[:-8])
        # print("Value :", val)
        # print("Length :", index)
        # print("First!11! :", test)  # This gets length from hub.
        totalMiles += tempTotalMiles
        # print("SECOND DIST: ", test)
        # setDelivered(test, keyListt, totalMiles)
        keyCounter = setDelivered(test, keyss, totalMiles, keyCounter, truckMilage)
        return findNxt(list, index, keyss, truckMilage, totalMiles, miles, keyCounter)

    # print("\n")

    for i, dist in enumerate(list):  # OK SO THIS CHECKS IF THE INDEX WE ARE USING IS NOW TOO BIG BECAUSE OF THE POP.  SHOULD WORK!
        # print(dist)
        try:
            length = len(list[index]) - 2
        except IndexError:
            index = index - 1
            # length = len(list[index - 1]) - 2
        finally:
            length = len(list[index]) - 2
            if length > len(
                    dist) - 2:  # If our length is greater than the current dist we are on, get the current dist length and find it on our length's row.
                sublength = len(dist) - 2
                # print(list[index][sublength + 1])  # Had to make elif because in case where they equal, I would get a repeated value.
                if float(list[index][sublength + 1]) < float(val):
                    val = list[index][sublength + 1]
                    newIndex = i
                    test = str(dist[1][:-8])
                    # print("Um Wut", keyListt)
                    # setDelivered(test, keyListt)
            elif length < len(
                    dist) - 2:  # If the length is less than the length of the dist we are checking, go to that row, and check our length against it.
                # print(list[i][length + 1])
                if float(list[i][length + 1]) < float(val):
                    val = list[i][length + 1]
                    newIndex = i
                    test = str(dist[1][:-8])

    # print("\n")
    # print("val...", val)
    # print("newIndex: ", newIndex)
    # print("Here it is: ", list[newIndex])
    # print(list)

    keyCounter = setDelivered(test, keyss, totalMiles, keyCounter, truckMilage)

    newList = list
    newList.pop(index)
    # print(newList)

    if val != 100.0:
        totalMiles += float(val)
        # print("total miles: ", totalMiles)

    if index < newIndex:
        newIndex -= 1

    return findNxt(newList, newIndex, keyss, truckMilage, totalMiles, miles, keyCounter)


timeCounter = []


def setDelivered(address, keys1, miles, keyCounter, truckMilage):
    print("KEYS!!!", keys1)
    # print("MILES: ", miles)
    # print((miles/18) * 60)
    # print(address)

    startTime = datetime.strptime('08:00', "%H:%M")  # Start Time.
    finalTime = startTime + timedelta(minutes=(miles / 18) * 60)
    finalTime = (str(finalTime)[11:])
    finalTime = (finalTime[:5])

    for key in keys1:
        if h.get(str(key), 1) == address:
            h.update(str(key), 7, "Delivered at " + finalTime)
            timeCounter.append((key, miles, truckMilage))
            print("Ran!", h.get(str(key), 0))
            keyCounter += 1

        if keyCounter == 16:
            return keyCounter

    return keyCounter


def setInDelivery(address, keys):
    amt = 0
    for key in keys:
        if h.get(key, 1) == address:
            h.update(key, 7, "Out for Delivery")
            amt += 1
    return amt


def timeConvert(myTime, bool=0):
    startTime = datetime.strptime('08:00', "%H:%M")  # Start Time.
    checkTime = datetime.strptime(str(myTime), "%H:%M")

    timeDifference = checkTime - startTime

    timeCheck = 18 * timeDifference.seconds / 3600  # Speed Distance Time Calculator

    if bool == 0:
        for i, timeCount in enumerate(timeCounter):
            if timeCounter[i][1] <= timeCheck:
                print(h.get(str(timeCounter[i][0]), None))
            elif timeCounter[i][2] <= timeCheck:
                tempStr = str(h.get(str(timeCounter[i][0]), None)[:-18])
                print(tempStr + 'En Route')
            else:
                tempStr = str(h.get(str(timeCounter[i][0]), None)[:-18])
                print(tempStr + 'At the Hub')
    else:
        print("Hello")
        print(bool)
        for i, timeCount in enumerate(timeCounter):
            # print(h.get(str(timeCounter[i][0]), 0))
            if int(h.get(str(timeCounter[i][0]), 0)) == bool:
                print(timeCounter[i][1])
                print(timeCheck)
                print("Here:", timeCounter[i][0])
                if timeCounter[i][1] <= timeCheck:
                    print(h.get(str(timeCounter[i][0]), None))
                elif timeCounter[i][2] <= timeCheck:
                    tempStr = str(h.get(str(timeCounter[i][0]), None)[:-18])
                    print(tempStr + 'En Route')
                else:
                    tempStr = str(h.get(str(timeCounter[i][0]), None)[:-18])
                    print(tempStr + 'At the Hub')


# TRUCK2--------------------------------------------------------------------------------------------------------------------------------------

delayed, delayedKeys = getCertainPackages('Delayed on flight---will not arrive to depot until 9:05 am', 7)
deliveredWith, deliveredWithKeys = getCertainPackages('Must be delivered with', 7)
wrongAddress, wrongAddressKeys = getCertainPackages('Wrong address listed', 7)
truck2, truck2Keys = getCertainPackages('Can only be on truck 2', 7)
whole, wholeKeys = getCertainPackages('UT', 3)
prime, primeKeys = getCertainPackages(':', 5)
eod, eodKeys = getCertainPackages('EOD', 5)

allKeys = list(range(1, 41))


deliveredWith.append(h.get(str(13), 1) + " (" + h.get(str(13), 4) + ")")  # This works!
deliveredWith.append(h.get(str(15), 1) + " (" + h.get(str(15), 4) + ")")
deliveredWith.append(h.get(str(19), 1) + " (" + h.get(str(19), 4) + ")")


newWhole = printDist(whole)
newDelayed = printDist(delayed)
newWrongAddress = printDist(wrongAddress)
newDeliveredWith = printDist(deliveredWith)
newTruck2 = printDist(truck2)
newPrimes = printDist(prime)
newEod = printDist(eod)

deliveredWithKeys.append('13')
deliveredWithKeys.append('15')
deliveredWithKeys.append('19')


print(len(newWhole))
print(deliveredWith)


firstRoute0 = newDeliveredWith + newTruck2
firstRoute = []
[firstRoute.append(element) for element in firstRoute0 if element not in firstRoute]

truck2Milage = findNxt(firstRoute, 'HUB', allKeys, 0)

print(truck2Milage)
print("\n")
print("\n")
print("\n")
print("\n")

truck2, truck2Keys = getCertainPackages('Can only be on truck 2', 7)
deliveredWith, deliveredWithKeys = getCertainPackages('Must be delivered with', 7)
whole, wholeKeys = getCertainPackages('UT', 3)
newTruck2 = printDist(truck2)
newDeliveredWith = printDist(deliveredWith)
newWhole = printDist(whole)

# So far...
prime, primeKeys = getCertainPackages(':', 5)
newPrimes = printDist(prime)

firstRoute = newWhole
#for value in newWrongAddress:
#      if value in firstRoute:
#         firstRoute.remove(value)

for value in newDelayed:
      if value in firstRoute:
         firstRoute.remove(value)




truck1Milage = findNxt(firstRoute, 'HUB', allKeys, 0, 0, 19.5)
print(truck1Milage)

#Truck1 Part 2-------------------------------------------------------------------------
print("\n")
print("\n")
print("\n")
print("\n")

truck2, truck2Keys = getCertainPackages('Can only be on truck 2', 7)
deliveredWith, deliveredWithKeys = getCertainPackages('Must be delivered with', 7)
delayed, delayedKeys = getCertainPackages('Delayed on flight---will not arrive to depot until 9:05 am', 7)
whole, wholeKeys = getCertainPackages('UT', 3)
prime, primeKeys = getCertainPackages(':', 5)

newTruck2 = printDist(truck2)
newDeliveredWith = printDist(deliveredWith)
newWhole = printDist(whole)
newDelayed = printDist(delayed)
newPrimes = printDist(prime)

firstRoute0 = newDelayed + newPrimes
firstRoute = []
[firstRoute.append(element) for element in firstRoute0 if element not in firstRoute]

allKeys.remove(9) # Make this better.
truck1Milage = findNxt(firstRoute, 'HUB', allKeys, truck1Milage, truck1Milage)
print(truck1Milage)


# Really hope this works........
print("\n")
print("\n")
print("\n")
print("\n")
if truck1Milage >= 42 or truck2Milage >= 42:
    h.update('9', 1, '410 S State St')
    h.update('9', 2, 'Salt Lake City')
    h.update('9', 4, '84111')
    h.update('9', 7, '')
    print("Ran I did")
    # print(h.get('9', None))
allKeys.append(9)
allKeys.remove(37)
allKeys.remove(38)
allKeys.remove(12)
whole, wholeKeys = getCertainPackages('UT', 3)
newWhole = printDist(whole)


print(wholeKeys)

truck2Milage = findNxt(newWhole, 'HUB', wholeKeys, truck2Milage, truck2Milage)

print(truck2Milage + truck1Milage)

print(truck2Milage + truck1Milage)

timeConvert("12:00", 11)