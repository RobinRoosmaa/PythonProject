class Person: #Loome klassi isikute objektide loomiseks.
    number_of_people = 0 #Selles kruppis on sisene muutuja, mis on isikute arv.
    GRAVITY = -9.8 #Sise muutuja lisamise näide, mida saab ainult selles kruppis muutujana kasutada.
    def __init__(self, name): #Algsel objekti loomisel küsitakse nime
        self.name = name #Objectile määratakse nimi.
        Person.add_person() #Kasutatakse isiku lisamise klassi meetodit, et lisada isik loendisse.
    @classmethod #Kasutatakse rida enne klassi meetodi loomist, mis on meetodid, mis ei kasuta objektide andmeid meetodi teostamiseks ja selle asemel kruppi siseseid muutujaid.
    def number_of_people_(cls): #Defineerime isikute numbri tagastus meetodi, mis toimib kõigi klassi objektidega.
        return cls.number_of_people #Tagastab isikute arvu väärtuse.
    @classmethod
    def add_person(cls): #Loome klassi meetodi, mis suurendab isikute loendit ühe võrra.
        cls.number_of_people += 1
#Testime programmi luues kaks isiku objekti ja küsides nende arvu.
p1 = Person("Tim")
p2 = Person("Tim")
print(Person.number_of_people_())