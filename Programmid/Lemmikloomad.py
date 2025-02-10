class Pet: #Ülema kruppi defineerimine, mida kasutavad alamad gruppid. Tähendus Lemmikloomad.
    def __init__(self, name, age): #Küsitakse kõigi lemmikloomade nime ja vanust esimesel objekti defineerimisel.
        self.name = name #Lemmikloom objektile määratakse antud nimi.
        self.age = age #Lemmikloom objektile määratakse antud vanus.
    def show(self): #Defineerime meetodi, millega saab kuvada nime ja vanust.
        print (f"I am {self.name} and I am {self.age} years old") #Kuvatakse objektile antud nime ja vanuse muutuja,
    def speak(self): #Defineerime meetodi, millega saab looma rääkima panna.
        print("I don't know what to say") #Määrame meetodile defauldi, mis kuvatakse kui alam kruppile pole antud speak meetodit.
class Cat(Pet): #Loome alam klassi lemmikloomad klassile, mis on kass objektide loomise jaoks.
    def __init__(self, name, age, color): #Määrame, et kass objektide loomisel on vaja sisestada ka värv.
        super().__init__(name, age) #Määrame, et alam grupp kasutaks nime ja vanuse seadmiseks juba defineeritud ülem kruppi meetodit vigade vältimiseks.
        self.color = color #Kass objektile määratakse antud värv.
    def speak(self): #Defineerime kassile eraldi speak käsu, mis eristub teistest lemmikloomadest.
        print("Meow") #Kuvab selle meetodi kassi peal kasutamisel "Meow".
    def show(self): #Defineerime kassile eraldi kuvamise käsu, mis eristub teistest lemmikloomadest.
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}") #Kuvame selle käigus ka värvi.
class Dog(Pet): #Loome samuti eraldi alam klassi koertele.
    def speak(self): #Defineerime koerale eraldi speak käsu, mis eristub teistest lemmikloomadest.
        print("Bark") #Kuvab selle meetodi kassi peal kasutamisel "Bark".

#Testime luues igat klassi looma ja andes neile kõik meetmed.
Lemmikloom = Pet("Tim", 19)
Lemmikloom.show()
Lemmikloom.speak()
Kass = Cat("Bill", 34, "Brown")
Kass.show()
Kass.speak()
Koer = Dog("Jill", 29)
Koer.show()
Koer.speak()