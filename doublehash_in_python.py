


class HashTable:
    def __init__(self):
        self.size = int(input(" Uneti Velicinu tabele (za ovaj zadatak uneti broj 7) : "))
        self.num = 3

        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0

    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    def h1(self, element):
        return element % self.size

    def h2(self, element):
        return 2 + (element % self.num)

    def doubleHashing(self, element, position):
        posFound = False
        limit = 20
        i = 2
        # start a loop to find the position
        newPosition = self.h1(element)
        while i <= limit:
            newPosition = (newPosition + self.h2(element)) % self.size
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                i += 1
        return posFound, newPosition

    def insert(self, element):
        if self.isFull():
            print("Hash Table Full")
            return False
        posFound = False
        position = self.h1(element)
        if self.table[position] == 0:
            self.table[position] = element
            print("Element " + str(element) + " na poziciji " + str(position))
            isStored = True
            self.elementCount += 1
        else:
            while not posFound:
                print("Kolizija elementa " + str(element) + " na poziciji " + str(
                    position) + " trazi se nova pozicija.")
                posFound, position = self.doubleHashing(element, position)
                if posFound:
                    self.table[position] = element
                    self.elementCount += 1
        return posFound

    def search(self, element):
        found = False
        position = self.h1(element)
        self.comparisons += 1
        if (self.table[position] == element):
            return position
        else:
            newPosition = position
            while i <= limit:
                position = (self.h1(element) + self.h2(element)) % self.size
                self.comparisons += 1
                if self.table[position] == element:
                    found = True
                    break
                elif self.table[position] == 0:
                    found = False
                    break
                else:
                    i += 1
            if found:
                return position
            else:
                print("Elementa nema")
                return found

    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " je obrisan")
            self.elementCount -= 1
        else:
            print("Elementa nema u tabeli")
        return

    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("Brojeva u tabeli ima : " + str(self.elementCount))

if __name__ == '__main__':

    table1 = HashTable()


    table1.insert(45)
    table1.insert(35)
    table1.insert(17)
    table1.insert(25)
    table1.insert(18)



    table1.display()
    print()
