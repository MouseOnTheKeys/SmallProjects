class Stack(object):
    def __init__(self, limit=10):
        self.vrednosti = [None] * limit
        self.limit = limit
        self.vrh = -1

    def push(self, value):
        if self.vrh == self.limit - 1:
            print("Stek je pun")
        else:
            self.vrh += 1
            self.vrednosti[self.vrh] = value

    def peek(self):
        if self.is_empty():
            print("Stekje prazan")
        else:
            return self.vrednosti[self.vrh]

    def print_stack(self):
        for i in range(self.vrh, -1, -1):
            print(self.vrednosti[i])

    def pop(self):
        if self.vrh == -1:
            return "Stek je prazan"
        else:
            vrednost = self.vrednosti[self.vrh]
            self.vrh -= 1
            return vrednost

    def is_empty(self):
        return self.vrh == -1


if __name__ == "__main__":

    """
    Domaci 1:
    U programskom jeziku Python. 
    Dat je pun stek od 10 elemenata (1,2,3,4,5,6,7,8,9,10).
    Potrebno je promeniti redosled elemenata na steku (10,9,8,7,6,5,4,3,2,1).
    """

    print("Domaci 1")

    def reverse_stack(stack):
        temp = Stack()

        while not stack.is_empty():
            temp.push(stack.pop())

        return temp

    stack = Stack()

    print("Da li je stack prazan: ", stack.is_empty())
    print("Ubaci 10 elemenata na stek: ...")

    for i in range(1, 11):
        stack.push(i)

    print("Stek :")
    stack.print_stack()
    print("")
    stack = reverse_stack(stack)
    print("Obrnuti stek: ")
    stack.print_stack()

    print("")

    """     
    Domaci 2:
    U programskom jeziku Python napisati klasu stek i nezavisnu funkciju def par_nepar(s1: Stack, s2: Stack, s3: Stack) 
    koja prima tri steka celih brojeva. 
    Smatrati da prvi stek s1 sadrži podatke (3, 1, 4, 1, 2, 6), a stekovi s2 i s3 su inicijalno prazni. 
    Funkcija treba da prerasporedi elemente iz steka s1 tako da na steku s2 budu svi parni, a na steku s3 svi neparni brojevi. 
    Na primer, ako su elementi u s1 bili (3, 1, 4, 1, 2, 6) onda nakon poziva funkcije dobija se s2=(4, 2, 6) i s3=(3, 1, 1).

    """

    print("domaci 2")
    print("")

    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    lst = [3, 1, 4, 1, 2, 6]

    for i in lst:
        s1.push(i)

    print("s1:")
    s1.print_stack()
    print("")

    def par_nepar(s1, s2, s3):
        while not s1.is_empty():
            if s1.peek() % 2 == 0:
                s2.push(s1.pop())
            else:
                s3.push(s1.pop())
        return s1, s2, s3

    par_nepar(s1, s2, s3)

    print("s2:")
    s2.print_stack()

    print("s3:")
    s3.print_stack()
