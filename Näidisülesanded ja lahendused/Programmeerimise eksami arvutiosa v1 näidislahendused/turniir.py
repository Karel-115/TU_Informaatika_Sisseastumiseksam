def loe_seis(faili_nimi):
    with open(faili_nimi, "r", encoding="UTF-8") as file:
        file.readline()
        sonastik = {}
        for rida in file:
            sonad = rida.split()
            sonad2=[]
            for sona in sonad[1:]:
                if sona != "-":
                    sonad2.append(int(sona))
                else:
                    sonad2.append(sona)
            sonastik[sonad[0]]=sonad2
        return sonastik

def lisa_tulemus(nimi, voor,sonastik,tulemus):
    #print(sonastik[nimi][voor-1])
    if sonastik[nimi][voor-1] != "-":
        print("Tulemus on juba varem lisatud!")
    else:
        sonastik[nimi][voor-1] = int(tulemus)
        print("Tulemus lisatud!")
    return sonastik

def leia_skoor(nimi,sonastik):
    skoor=0
    for tulemus in sonastik[nimi]:
        if tulemus != "-":
            skoor += tulemus
    return skoor
    
#loe_seis("turniir.txt")
#lisa_tulemus("Mari", 3, loe_seis("turniir.txt"), 0)
#leia_skoor("Malle", loe_seis("turniir.txt"))

sonastik = loe_seis("turniir.txt")

while True:
    print("Vali tegevus:")
    print("1 - Vaata punktitabelit")
    print("2 - Lisa tulemus")
    print("3 - Vaata skoori")
    print("4 - Leia võitja")
    print("5 - Lõpeta programmi töö")
    valik = int(input())
    if valik == 1:
        #sonastik = loe_seis("turniir.txt")
        for inimene in sonastik:
            print(inimene, end=" ")
            for voor in sonastik[inimene]:
                print(voor, end=" ")
            print()
    if valik == 2:
        nimi = str(input("Sisesta nimi: "))
        voor = int(input("Sisesta voor: "))
        tulemus = int(input("Sisesta punktid: "))
        lisa_tulemus(nimi, voor, sonastik, tulemus)
    if valik == 3:
        nimi = str(input("Sisesta nimi: "))
        skoor = leia_skoor(nimi, sonastik)
        print("Mari skoor on " + str(skoor) + ".")
    if valik == 4:
        suurim = ("",0)
        for nimi in sonastik:
            skoor = leia_skoor(nimi, sonastik)
            if skoor > suurim[1]:
                suurim = (nimi,skoor)
        print("Suurima skooriga on " + str(suurim[0]) + " (" + str(suurim[1]) +" punkti).")
    if valik == 5:
        fail = open("turniir_uus.txt", "w")
        #voorude_kogus = 0
        indeks = 0
        for nimi in sonastik:
            if indeks == 0:
                #voorude_kogus = len(sonastik[nimi])
                #voorude_rida = "     "
                fail.write("     ")
                for voorude_kogus in range(len(sonastik[nimi])):
                    fail.write(str(voorude_kogus) + " ")
                    #voorude_rida += str(voorude_kogus) + " "
                fail.write("\n")
            indeks += 1
            skoor = ""
            for voor in sonastik[nimi]:
                skoor = skoor + str(voor) + " "
            if indeks == len(sonastik):
                skoor = nimi + " " + skoor
            else:
                skoor = nimi + " " + skoor + "\n"
            #print(skoor)
            fail.write(skoor)
        fail.close()
        print("Programm lõpetas töö.")
        break


