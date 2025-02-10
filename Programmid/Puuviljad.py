#Puuviljade defineerimise klassi loomine.
class Fruit:
    def __init__(self, name, clr): #Määrame init ehk algatus funktsiooni, mis on kasutajalt nõutud muutujad, et objekt saaks klassifikatsiooni.
        self.name = name #Puuvilja objektile määratud nimi
        self.colour = clr #Puuvilja objektile määratud värv
    def details(self): #Meetodi loomine, millega saab küsida tetaile puuvilja kohta.
        print("my " + self.name + " is " + self.colour) #Meetodi esimene tegevus, mis kuvab nii loodud puuvilja objecti nime ja värvi.
        exp_date = "07.20.2021" #Puuvilja aegumiskuupäev, mis on meetodi sisene muutuja ja pole kasutatav mujal.
        print("expires on " + exp_date) #Tegevus antud meetodile, mis on aegumiskuupäeva printimine.
apple = Fruit("apple", "red") #Programmi katsetus objekti loomisega, mis on puuvili õun värvi väärtusega punane ja nime väärtusega apple.
apple.details() #Puuviljade klassile antud meetodi katsetamine. Näha on, et puuviljad klassi objectina on õunal see olemas.