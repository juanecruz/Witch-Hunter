class Carta:
    a = ["AS",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    b = ["picas","corazones","diamantes","treboles"]
    def __init__(self,n,o):
        self.num = n
        self.obj = o
    def __str__(self):
        msn ="{0} de {1}".format(self.a[self.num],self.b[self.obj])
        return msn
    def comparar(self,card):
        if self.num == card.num:
            return 0
        elif self.num > card.num:
            return 1
        elif self.num > card.num:
            return -1
        else:
            return 0
    def __lt__(self, card):
        if self.comparar(card)<0:
            return True
        else:
            return False
    def __gt__(self,card):
        if 0 > self.comparar(card):
            return False
        else:
            return True
class Baraja:
        
    def __init__(self):
        self.cartas = []
        for e in range(4):
            for j in range(13):
                self.cartas.append(Carta(j,e))
    def __str__(self):
        msn = ""
        for c in self.cartas:
            msn += str(c) + "\n"
        return msn
    def barajat(self):
        import random
        rnd = random.Random()
        rnd.shuffle.Random()
        rnd.shuffle(self.cartas)
    def sacar_carta(self,card):
        if card in self.cartas:
             del self.cartas.remove[card]
            return True
        else:
            return False
c1 = Carta(1,0)
print(c1)
b_roja = Baraja()
b_roja.sacar_carta(c1)
print(b_roja)
        

        
        

