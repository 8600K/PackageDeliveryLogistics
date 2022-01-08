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

    def add(self, key, v0, v1, v2, v3, v4, v5):
        hashedKey = self.getHash(key)
        values = [key, v0, v1, v2, v3, v4, v5]

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
                    return True
            self.map[hashedKey].append(values)
            return True

    def getData(self, csvInput):
        with open(csvInput, mode='r', encoding='utf-8') as fileInput:

            csvFile = csv.reader(fileInput)

            keys = 0
            for row in csvFile:
                if row[0].isnumeric():
                    self.add(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                else:
                    continue
                keys += 1
        return keys

    def get(self, key, rows):
        hashedKey = self.getHash(key)
        if self.map[hashedKey] is not None:
            for pair in self.map[hashedKey]:  # Expand upon this.  Should have a feature to get options directly.
                if pair[0] == key:
                    if rows == None:
                        return str(pair[1]) + " " + str(pair[2]) + " " + str(pair[3]) + " " + str(pair[4]) + " " + str \
                            (pair[5]) + " " + str(pair[6])
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
def getVipPackages():
    i = 1
    prime = []
    while i <= keyAmount:

        word = 'EOD'
        tempStr = h.get(str(i), 5)
        if word not in tempStr:
            prime.append(h.get(str(i), 1) + " (" + h.get(str(i), 4) + ")" + ":" + tempStr)
        i += 1

    for i, primes in enumerate(prime):
        prime[i] = prime[i].split(':')[0]

    return prime


# START OF THE ALGORITHM


primes = getVipPackages()


# print(distList[1][1])

def printDist():
    for i in distList:
        for j in primes:
            if (j == i[1]):
                # print("FOUND!", i)
                c = len(i) - 1
                print(i[1:len(i) - 1])
                continue
        # print(i [1:len(i)])

#Commit!
# THIS IS JUST FINDING THE FASTEST ROUTE. NO PRIME PACKAGES
some = 100.0
index = None
for i, dist in enumerate(distList):

    # print(dist[2])\
    try:
        float(dist[2])
    except ValueError:
        None
    else:
        if 0.0 < float(dist[2]) < float(some):
            some = dist[2]
            index = i

print(some)
print(index)
# printDist()
print(distList[20])
print(len(distList[20]))
# 23
# print(distList[21][22])

tempLow = 256
print("Check", distList[20])  # - 2???
for j, dist in enumerate(distList):
    if j > 20:
        print(dist[23 - 1])
        x = float(dist[23 - 1])
        if x < tempLow:
            tempLow = x
print("TempLow y AXIS: ",tempLow)


# for sublist in distList:
# for i in range(len(primes)):
# if primes[i] == sublist[1]:
# print(primes[i])
# print(sublist)
# continue
# list(set(primes).intersection(distList))


# 5383 South 900 East #104 (84117)

# for sublist in distList:
#    if sublist[1] == primes[7]:
#        print("Found it!", sublist)
#        break


# EG At the Hub, En Route, Or Delivered.
# 0: Package ID | 1: Address | 2: Deadline | 3: City | 4: Zip Code | 5: Weight | 6: Delivery Status
