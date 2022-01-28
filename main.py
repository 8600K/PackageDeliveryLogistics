# Miles Engelbrecht | Student ID #001435519


import csv
from datetime import datetime

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
                        return str(pair[1]) + " " + str(pair[2]) + " " + str(pair[3]) + " " + str(pair[4]) + " " + str \
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
                    print("This ran!  Good job.")

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
def getCertainPackages(word, index):
    i = 1
    prime = []
    keyList = []
    while i <= keyAmount:

        # ALSO CHECK THAT IT'S AT HUB!
        # word = 'EOD'
        tempStr = h.get(str(i), index)
        if word in tempStr and h.get(str(i), 7 != 'Delivered'):
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


# Commit!
# THIS IS JUST FINDING THE FASTEST ROUTE. NO PRIME PACKAGES


print("\n")


def findNxt(list, index, keyListt, totalMiles=0, miles=0):
    if len(list) == 1:
        print("This ran!  !  !")
        totalMiles += float(list[0][2])  # Gets us back to the hub.
        # print("Should be 3.7...? ", val)
        return totalMiles

    if totalMiles < miles != 0 and totalMiles != 0: # NOTE...
        if totalMiles + float(list[int(index)][2]) >= miles:
            totalMiles += float(list[index][2])
            print("And here we returned... ", list[index][2])
            print("Total Miles: ", totalMiles)
            return totalMiles
    elif totalMiles > miles != 0:
        print("And here we returned electric 2: ", list[index][2])
        totalMiles += float(list[index][2])
        print("Total Miles: ", totalMiles)
        return totalMiles

    newIndex = None
    val = 100.0
    test = None
    if (index == 'HUB'):
        for i, dist in enumerate(list):
            print(dist[2])
            if float(dist[2]) < val:
                val = float(dist[2])
                totalMiles = val
                index = i
                test = dist[1][:-8]
                # print("Here it is! ",test[:-8])
        print("Value :", val)
        print("Length :", index)
        print("First!11! :", test)  # This gets length from hub.
        # print("SECOND DIST: ", test)
        # setDelivered(test, keyListt, totalMiles)
        return findNxt(list, index, keyListt, totalMiles, miles)

    print("\n")

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
                print(list[index][
                          sublength + 1])  # Had to make elif because in case where they equal, I would get a repeated value.
                if float(list[index][sublength + 1]) < float(val):
                    val = list[index][sublength + 1]
                    newIndex = i
                    test = str(dist[1][:-8])
                    # print("Um Wut", keyListt)
                    # setDelivered(test, keyListt)
            elif length < len(
                    dist) - 2:  # If the length is less than the length of the dist we are checking, go to that row, and check our length against it.
                print(list[i][length + 1])
                if float(list[i][length + 1]) < float(val):
                    val = list[i][length + 1]
                    newIndex = i
                    test = str(dist[1][:-8])

    print("\n")
    print("val...", val)
    print("newIndex: ", newIndex)
    print("Here it is: ", list[index])
    setDelivered(test, keyListt, totalMiles)

    newList = list
    newList.pop(index)
    print(newList)

    if val != 100.0:
        totalMiles += float(val)
        print("total miles: ", totalMiles)

    if index < newIndex:
        newIndex -= 1

    return findNxt(newList, newIndex, keyListt, totalMiles, miles)


timeCounter = []

def setDelivered(address, keys, miles):
    print("KEYS!!!", keys)
    for key in keys:
        if h.get(str(key), 1) == address:
            h.update(str(key), 7, "Delivered")
            # TODO Do that shit.
            timeCounter.append( (key, miles) )
            print("Ran!")


def setInDelivery(address, keys):
    amt = 0
    for key in keys:
        if h.get(key, 1) == address:
            h.update(key, 7, "Out for Delivery")
            amt += 1
    return amt

def timeConvert(myTime):
    startTime = datetime.strptime('08:00', "%H:%M") # Start Time.
    checkTime = datetime.strptime(str(myTime), "%H:%M")

    timeDifference = checkTime - startTime

    timeCheck = 18 * timeDifference.seconds / 3600 # Speed Distance Time Calculator
    print("This should be 13.5", timeCheck)

    for i, timeCount in enumerate(timeCounter):
        if timeCounter[i][1] <= timeCheck:
            print(h.get(str(timeCounter[i][0]), None))




    #for i in timeCounter:


    # Set progress!
    # Can set the out for delivery once I run this program.  Make new function?
    # Set delivered somehow...

    # Return total miles.
    # Return listNumber.
    # Recursive this?

    # for dist in list:
    #    print(dist[len(dist) - 2])


# START OF THE ALGORITHM


# primes = getPrimePackages('EOD')

# primes, keyList = getCertainPackages(':', 5)  # Let's go!

# print(primes)

# eod, keyList = getCertainPackages('EOD', 5)
# print(eod)

# print("Hash: ", h.getHash(1))
# print("H: ", h.get('1', 1))

# truck2, keyList = getCertainPackages('Can only be on truck 2', 7)
# print("Keys: ", keyList)
# print(truck2)

delayed, delayedKeys = getCertainPackages('Delayed on flight---will not arrive to depot until 9:05 am', 7)
# print("CHCK", delayed) Works.


deliveredWith, deliveredWithKeys = getCertainPackages('Must be delivered with', 7)
# print(goWith)

wrongAddress, wrongAddressKeys = getCertainPackages('Wrong address listed', 7)
# print(wrongAddress)

whole, keyListt = getCertainPackages('UT', 3)

allKeys = list(range(1, 41))
print("Should print all keys: ", allKeys)

print(deliveredWith)
deliveredWith.append(h.get(str(13), 1) + " (" + h.get(str(13), 4) + ")")  # This works!
deliveredWith.append(h.get(str(15), 1) + " (" + h.get(str(15), 4) + ")")
deliveredWith.append(h.get(str(19), 1) + " (" + h.get(str(19), 4) + ")")
print(deliveredWith)

# newPrimes = printDist(primes)
# newTruck2 = printDist(truck2)


newWhole = printDist(whole)
newDelayed = printDist(delayed)
newWrongAddress = printDist(wrongAddress)
newDeliveredWith = printDist(deliveredWith)

print("\n")

print("newDeliveredWith: ", newDeliveredWith)
print(len(newDeliveredWith))

# Probably change this to second route
firstRoute = [element for element in newWhole if element not in newDelayed]
firstRoute = [element for element in firstRoute if element not in newWrongAddress]
firstRoute = [element for element in firstRoute if element not in newDeliveredWith]

print("First Route... ", firstRoute)
print(len(firstRoute))
print(len(newWhole))
# Seems to be working.

print("\n")

# So change this to truck 2...?

truck2 = findNxt(firstRoute, 'HUB', allKeys, 0, 19.5)
newWhole = printDist(firstRoute)

print("Check", truck2)

#list_difference = [item for item in newWhole if item not in woah]
#print("\n")
#print("This is it! ", list_difference)
#print(len(list_difference))
print("\n")

print(h.get('32', 1))

print("\n")

h.print()

truck2, keyList = getCertainPackages('Can only be on truck 2', 7)

newTruck2 = printDist(truck2)

print(newTruck2)



print("\n")

# print(h.get(str('15'), None))

print(timeCounter)


timeConvert('8:45')

# UP TO HERE WORKS LIKE A CHARM.

delayed, delayedKeys = getCertainPackages('Delayed on flight---will not arrive to depot until 9:05 am', 7)
# print("CHCK", delayed) Works.


deliveredWith, deliveredWithKeys = getCertainPackages('Must be delivered with', 7)
# print(goWith)

wrongAddress, wrongAddressKeys = getCertainPackages('Wrong address listed', 7)

whole, keyListt = getCertainPackages('UT', 3)

newWhole = printDist(whole)
newDelayed = printDist(delayed)
newWrongAddress = printDist(wrongAddress)
newDeliveredWith = printDist(deliveredWith)

secondRoute = [element for element in newWhole if element not in newDelayed]
secondRoute = [element for element in secondRoute if element not in newWrongAddress]
secondRoute = [element for element in secondRoute if element not in truck2]

print(len(secondRoute))
for i in secondRoute:
    print(i)

woah1 = findNxt(secondRoute, 'HUB', keyListt)




# print(eod)
# newEod = printDist(eod)
# print(newTruck2)
# print("double check:", keyList)
# print("Amt: ", len(newEod))

# print("newPrimes: ", newPrimes)
# print(newEod)
# print(newWhole)
# print(newTruck2)
# print(newDelayed)
# print("Check!", newEod)
# print(newTruck2)

# newWhole = (set(newWhole))

# miles = findNxt(newTruck2, 'HUB', keyList, 0)

# print("Miles: ", miles)

# delay = findNxt(newDelayed, 'HUB')

# print("Delayed Miles: ", delay)

# Some round feature here?  Python seems to want to be deathly accurate, lol.

# prime = findNxt(newPrimes, 'HUB', keyList)

# end = findNxt(newEod, 'HUB', keyList, 0)

# print("Miles: ", end)
