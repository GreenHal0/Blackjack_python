from random import shuffle


class Carte:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        if self.value == 1:
            self.value = 11
            self.nom = "As" + " " + str(color)
        elif self.value == 11:
            self.value = 10
            self.nom = "Valet" + " " + str(color)
        elif self.value == 12:
            self.value = 10
            self.nom = "Dame" + " " + str(color)
        elif self.value == 13:
            self.value = 10
            self.nom = "Roi" + " " + str(color)
        else:
            self.nom = str(value) + " " + str(color)

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def getName(self):
        return self.nom

    def setValue(self, x):
        self.value = x


class JeuDeCarte:
    def __init__(self):
        self.jeu = []
        self.couleurs = ["Pic", "Coeurs", "Trefle", "Carreaux"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        self.create()

    def create(self):
        for k in range(6):
            for i in range(len(self.couleurs)):
                for j in range(len(self.numbers)):
                    self.jeu.append(Carte(self.numbers[j], self.couleurs[i]))

    def getJeu(self):
        for i in range(len(self.jeu)):
            print(self.jeu[i].getName())

    def shuf(self):
        for i in range(4):
            shuffle(self.jeu)
        return self.jeu

    def distribuer(self):
        card = self.jeu[0]
        del self.jeu[0]
        return card

    def longueur(self):
        return len(self.jeu)


Victoires = 0
Defaites = 0

Main = []
Croupier = []


def Manche():
    print('\r')
    z = 0

    if jeu.longueur() <= 20:
        jeu.create()
        jeu.shuf()
        print("Le jeud a été mélangé à nouveau.")

    Main.append(jeu.distribuer())
    Croupier.append(jeu.distribuer())
    Main.append(jeu.distribuer())
    Croupier.append(jeu.distribuer())

    print("Votre main :", Main[0].getName(), ",", Main[1].getName())
    print("Total =", Main[0].getValue() + Main[1].getValue())
    print("Main du croupier :", Croupier[0].getName())

    somme_main = Main[0].getValue() + Main[1].getValue()
    somme_croupier = Croupier[0].getValue() + Croupier[1].getValue()

    print()
    choix = 1

    while somme_main <= 21 and choix == 1:
        choix = int(input("1 = Tirer, 2 = Rester. Choix : "))
        print("")
        if choix == 1:
            Main.append(jeu.distribuer())
            somme_main += Main[len(Main) - 1].getValue()

            if somme_main > 21:
                for i in range(len(Main)):
                    if Main[i].getValue() == 11:
                        Main[i].setValue(1)
                        somme_main -= 10

            print("Nouvelle main du joueur : ", end="")
            for i in range(len(Main)):
                print(Main[i].getName(), end=", ")
            print("")
            print("Totale =", somme_main)
            print("")

        elif choix == 2:
            somme_main = somme_main

    print('\r')

    if somme_main > 21:
        z = 1
        gagnant(0, 0, z)

    else:
        print("Main du croupier :", Croupier[0].getName(), ",",
              Croupier[1].getName())
        print("Total =", somme_croupier)
        print("")
        while somme_croupier < 17:
            Croupier.append(jeu.distribuer())
            print("Nouvelle main du croupier : ", end="")
            for i in range(len(Croupier)):
                print(Croupier[i].getName(), ",", end=" ")
            print("")
            somme_croupier += Croupier[len(Croupier) - 1].getValue()
            print("Totale =", somme_croupier)
            print("")

            if somme_main > 21:
                for i in range(len(Main)):
                    if Main[i].getValue() == 11:
                        somme_croupier -= 10

        print("")

    if somme_croupier > 21:
        z = 2
        gagnant(0, 0, z)

    elif z == 0:
        gagnant(somme_main, somme_croupier)


def gagnant(x, y, z=0):
    global Victoires, Defaites, Main, Croupier
    if z == 1:
        print("Main du croupier :", Croupier[0].getName(), ",",
              Croupier[1].getName())
        print("Total =", Croupier[0].getValue() + Croupier[1].getValue())
        print("Le joueur à sauté")
        print()
        Defaites += 1
    elif z == 2:
        print("Le croupier à sauté.")
        print("Victoire du joueur.")
        Victoires += 1
    elif x > y:
        print("Le joueur à gagner.")
        print()
        Victoires += 1
    elif x < y:
        print("Le croupier à gagner.")
        print()
        Defaites += 1
    else:
        print("Egalité parfaite.")
        print()

    Main.clear()
    Croupier.clear()

    replay = '/'
    while replay != 'o' and replay != 'n':
        replay = input("Voulez-vous rejouer ? (o/n)")
    if replay == 'o':
        Manche()
    else:
        print("A bientôt ! (Manche() pour rejouer)")


def winrate():
    global Victoires, Defaites
    print("Victoires :", Victoires)
    print("Defaites :", Defaites)
    print("Winrate :", (Victoires / (Victoires + Defaites) * 100), "%")


def init():
    jeu.shuf()
    f = open('init.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    Manche()

jeu = JeuDeCarte()
init()
