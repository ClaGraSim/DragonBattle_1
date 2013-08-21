import random
#Schadensmodell
#-----------------------------
#Heiltrank = 1
#Ausweichen = E.Feuer: 0.5
#Ausweichen = E.Blick: 0.75
#Ausweichen = Schlitzer: 1
#Verstecken = E.Feuer: 1
#Verstecken = E.Blick: 0.5
#Verstecken = Schlitzer: 0.25
#Verteidigen = E.Feuer: 0.75
#Verteidigen = E.Blick: 1
#Verteidigen = Schlitzer: 0.5 
#-----------------------------
s={}
s["Enderdragonfeuer"]={"Ausweichen":0.5,"Verstecken":1,"Verteidigen":0.75,"Heiltrank trinken":1}
s["Enderdragonblick"]={"Ausweichen":0.75,"Verstecken":0.5,"Verteidigen":1,"Heiltrank trinken":1}
s["Schlitzer"]={"Ausweichen":1,"Verstecken":0.25,"Verteidigen":0.5,"Heiltrank trinken":1}

b="Enderdragon"
spieler="Keanu"
bhp=100
shp=20
heiltrank=4
minschaden=0
maxschaden=7
runde=0
krit=0.2
aus=0.6
eilegen=0.1
verteidigen=False
verstecken=False
ausweichen=False
schlag1=0.75
schlag2=0.5
schlag3=0.25
menua=["Spiel beenden",
       "Normaler Angriff",
       "Ultimativer Angriff",
       "Magie Angriff",
       "Doppelschlag"]
menub=["Spiel beenden",
       "Verteidigen",
       "Verstecken",
       "Ausweichen",
       "Heiltrank trinken"]
Enderdragonaction=["Schlitzer",
             "Enderdragonfeuer",
             "Enderdragonblick"]

while bhp > 0 and shp > 0:
        runde=runde+1
        while True:
            for x in menua:
                print(menua.index(x),x)
            x=input()
            if x < "0" or x > "4" or len(x)>1:
                print("FALSCHE EINGABE !!!!!")
                continue
            else:
                print()
                break
        #Menü von dem Spieler
        if x == "0":
            print("Du wurdest vom",b,"besiegt!")
            break
        elif x == "1":
            print("Runde",runde)
            print("--------------------")
            print(spieler,"greift an!")
            schaden=random.randint(minschaden, maxschaden)
            print(b,"erleidet",schaden,"Schaden")
            bhp=bhp-schaden
            print(b,"hat noch",bhp,"Herzen")
            print("()"*int(bhp))
            print()
        elif x == "2":
            print("Runde",runde)
            print("--------------------")
            print("Du versuchst den Ultimativen ANGRIFF!")
            print()
            treffer=random.random()
            if treffer < krit:
                print("Der Ultimative Angriff ist gelungen!")
                schaden=maxschaden*2
                print(b,"erleidet",schaden,"Schaden")
                bhp=bhp-schaden
                print(b,"hat noch",bhp,"Herzen")
                print("()"*int(bhp))
                print()
            else:
                print("Der Ultimative Angriff ist dir nicht gelungen!")
                print()
        elif x == "3":
            print("Runde",runde)
            print("--------------------")
            print(spieler,"greift mit Magie an!")
            schaden=random.randint(3, 5)
            print(b,"erleidet",schaden,"Schaden")
            bhp=bhp-schaden
            print(b,"hat noch",bhp,"Herzen")
            print("()"*int(bhp))
            print()
        elif x == "4":
            print("Runde",runde)
            print("--------------------")
            print(spieler,"greift mit dem Doppelschlag an!")
            schaden=2
            print(b,"verliert",schaden,"Herzen!")
            bhp=bhp-schaden
            print(b,"hat noch",bhp,"Herzen!")
            print()
            schlag=random.random()
            if schlag < schlag1:
                    print("Du hast einen zweiten Treffer gelandet!")
                    schaden=2.5
                    print(b,"verliert",schaden,"Herzen!")
                    bhp=bhp-schaden
                    print(b,"hat noch",bhp,"herzen!")
                    schlag=random.random()
            if schlag < schlag2:
                    print("Du hast einen dritten Treffer gelandet!")
                    schaden=3.5
                    print(b,"verliert",schaden,"Herzen!")
                    bhp=bhp-schaden
                    print(b,"hat noch",bhp,"Herzen!")
                    schlag=random.random()
            if schlag < schlag3:
                    print("Du hast einen vierten Treffer gelandet!")
                    schaden=4
                    print(b,"verliert",schaden,"Herzen!")
                    bhp=bhp-schaden
                    print(b,"hat noch",bhp,"Herzen!")
            else:
                    print("Das waren deine Angriffe!")
        #Menü 2 von dem Spieler
        verteidigen=False
        verstecken=False
        ausweichen=False
        while True:
            for x in menub:
                print(menub.index(x),x)
            x=input()
            if x < "0" or x > "4" or len(x)>1:
                print("FALSCHE EINEGABE !!!!!")
                continue
            else:
                print()
                break
        if x == "0":
                print("Du wurdest vom",b,"besiegt!")
                break
       
        elif x == "4":
             print(spieler,"trinkt einen Heiltrank!")
             print()
             heiltrank=random.randint(7, 12)
             print(spieler,"hat",heiltrank,"Herzen bekommen!")
             shp=shp+heiltrank
             print(spieler,"hat jetzt",shp,"Herzen!")
             print("o"*int(shp))
             print()         
        #Enderdragon schlägt zurück
        action=random.choice(Enderdragonaction)
        if action == "Schlitzer":
            print("Der",b,"schlägt mit seinen Flügeln auf dich ein!")
            print()
        elif action == "Enderdragonfeuer":
            print("Der",b,"spuckt auf dich mit Feuer!")
            print()
        elif action == "Enderdragonblick":
            print("Der",b,"blickt dich mit einem Magieblick an")
            print()
        #Schadensberechnung
        schaden=s[action][menub[int(x)]]*random.randint(4, 7)
        if schaden == 0:
                print("Das war perfekt!")
        elif schaden <= 5:
                print("Das war ziemlich gut!")
        elif schaden == 5:
                print("Du bist ein middle!")
        elif schaden >= 5:
                print("Das war schlecht!")
        elif schaden >= 10:
                print("Du bist der schlechteste Spieler in diesem Spiel!")
        print("Du erleidest Schaden:",schaden)
        shp=shp-schaden
        print("Du hast noch",shp,"Herzen")
        print("o"*int(shp))
        print()
        
if bhp <= 0:
    print(b, "wurde von" ,spieler, "besiegt!")
    
if shp <= 0:
    print(spieler, "wurde von" ,b, "besiegt!")
