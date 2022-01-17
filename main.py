# Miles Engelbrecht | Student ID #001435519


import csv


# No duplicate keys.
# O(1) for add, get, delete functions.

# def _get_hash(self, key):
#   hash = 0
#    for char in str(key):
#        hash += ord(char)
#    return hash % self.size


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
    while i <= keyAmount:

        # word = 'EOD'
        tempStr = h.get(str(i), index)
        if word in tempStr:
            prime.append(h.get(str(i), 1) + " (" + h.get(str(i), 4) + ")" + ":" + tempStr)
        i += 1

    for i, primes in enumerate(prime):
        prime[i] = prime[i].split(':')[0]

    return prime


# START OF THE ALGORITHM


# primes = getPrimePackages('EOD')

primes = getCertainPackages('EOD', 5)
#print(primes)

truck2 = getCertainPackages('Can only be on truck 2', 7)
#print(truck2)

delayed = getCertainPackages('Delayed on flight---will not arrive to depot until 9:05 am', 7)
#print(delayed)

goWith = getCertainPackages('Must be delivered with', 7)
#print(goWith)

wrongAddress = getCertainPackages('Wrong address listed', 7)
#print(wrongAddress)








def printDist(sublist):
    returnList = []
    for i in distList:
        for j in sublist:
            if (j == i[1]):
                # print("FOUND!", i)
                c = len(i) - 1
                # print(i[0:len(i)])
                returnList.append(i[0:len(i) ])
                continue
    return returnList

        # print(i [1:len(i)])


# Commit!
# THIS IS JUST FINDING THE FASTEST ROUTE. NO PRIME PACKAGES

newTruck2 = printDist(truck2)
newDelayed = printDist(delayed)
newPrimes = printDist(primes)

print(newTruck2)
print(newDelayed)

def findNext(col, row, used, list):
    val = 100.0
    for i, dist in enumerate(list):
        if i >= col:
            try:
                float(dist[row])
            except ValueError:
                None
            else:
                if 0.0 < float(dist[row]) < float(val):
                    val = dist[row]
                    print(dist)
                    index = distList.index(dist)

    if(used != 'HUB'):
        for i in range(2, len(distList[row]) - 1):
            if float(list[row][i]) != used and float(list[row][i]) < float(val) and float(list[row][i] != 0.0):
                val = list[row][i]
                index = distList.index(dist)
                print(distList[i])
                # Obv test this more but we should be in business.

    return val, index


# sublist = [distList]

def findNxt(list, index, totalMiles):

    if(len(list) == 0):  # Could also check for list having one value.  Should also work.
        print("Does this ever run?")
        return totalMiles

    newIndex = None
    val = 100.0
    if(index == 'HUB'):
        for i, dist in enumerate(list):
            print(dist[2])
            if float(dist[2]) < val:
                val = float(dist[2])
                totalMiles = val
                index = i
        print("Value :", val)
        print("Length :", index) # This gets length from hub.
        return findNxt(list, index, totalMiles)


    print("\n")

    for i, dist in enumerate(list):  # OK SO THIS CHECKS IF THE INDEX WE ARE USING IS NOW TOO BIG BECAUSE OF THE POP.  SHOULD WORK!
        # print(dist)
        try:
            length = len(list[index]) - 2
        except IndexError:
            print("Broke...?")
            index = index - 1
            # length = len(list[index - 1]) - 2
            print("Nope!")
        finally:

            #print("PREBREAK: ", index)
            #print("THIS IS WHAT BREAKS: ", len(list[index]))
            length = len(list[index]) - 2
            if length > len(dist) - 2: # If our length is greater than the current dist we are on, get the current dist length and find it on our length's row.
                sublength = len(dist) - 2
                print(list[index][sublength + 1])  # Had to make elif because in case where they equal, I would get a repeated value.
                if float(list[index][sublength + 1]) < float(val):
                    val = list[index][sublength + 1]
                    newIndex = i
            elif length < len(dist) - 2:  # If the length is less than the length of the dist we are checking, go to that row, and check our length against it.
                print(list[i][length + 1])
                if float(list[i][length + 1]) < float(val):
                    val = list[i][length + 1]
                    newIndex = i
    print("\n")
    print("val...", val)
    print("newIndex: ",newIndex)
    newList = list
    newList.pop(index)
    print(newList)


    if val != 100.0:
        totalMiles += float(val)
        print("total miles: ", totalMiles)
    return findNxt(newList, newIndex, totalMiles)





        # Return total miles.
        # Return listNumber.
        # Recursive this?


    #for dist in list:
    #    print(dist[len(dist) - 2])










#miles = findNxt(newTruck2, 'HUB', 0)

#print("Miles: ", miles)

delay = findNxt(newDelayed, 'HUB', 0)

print("Delayed Miles: ", delay)

# Some round feature here?  Python seems to want to be deathly accurate, lol.

#prime = findNxt(newPrimes, 'HUB', 0)

#print(prime)

#print(distList.index('1060 Dalton Ave S (84104)', 1, 2))
#print(distList.index(['International Peace Gardens 1060 Dalton Ave S', '1060 Dalton Ave S (84104)', '7.2', '0.0']))


# NODE distList should start at 0,2, ANY LIST THAT HAS BEEN RUN THROUGH GETCERTAINPACKAGES THE 2 SHOULD BE 1!!!




















def XAxis(row, used):
    val = 100.0
    leng = len(distList[row])
    for i in range(2, len(distList[row]) - 1):
        if float(distList[row][i]) != used and float(distList[row][i]) < float(val):
            val = distList[row][i]
    return val

# val, index = YAxis(index, leng)


# EG At the Hub, En Route, Or Delivered.
# 0: Package ID | 1: Address | 2: Deadline | 3: City | 4: Zip Code | 5: Weight | 6: Delivery Status
