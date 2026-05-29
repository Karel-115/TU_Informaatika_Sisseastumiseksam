def loe_tulemused(faili_nimi):
    with open(faili_nimi, "r", encoding="UTF-8") as file:
        sonastik = {}
        for rida in file:
            rida = rida.strip()
            sonad = rida.split(";")
            #print(sonad)
            sonad2=[]
            for sona in sonad[1:]:
                    sonad2.append(sona)
            sonastik[sonad[0]]=sonad2
        return sonastik
    
def lisa_tulemus(sonastik):
    nimi = str(input("Nimi: "))
    tulemus = str(input("Tulemus(W/L): "))
    if nimi in sonastik:
        sonastik[nimi].append(tulemus)
    else:
        sonastik[nimi]=[tulemus]
    print("Tulemus lisatud!")
    return sonastik

def leia_võitude_arv(sonastik,nimi):
    count = 0
    for match in sonastik[nimi]:
        if match == "W":
            count += 1
    return count

def leia_parim(sonastik):
    parim = ("",0)
    for nimi in sonastik:
        võitude_arv = leia_võitude_arv(sonastik,nimi)
        if võitude_arv > parim[1]:
            parim = (nimi,võitude_arv)
    print("Parim on " + str(parim[0]) + " " + str(parim[1]) + " võiduga")
#lisa_tulemus(loe_tulemused("tulemused.txt"))

sonastik = loe_tulemused("tulemused.txt")

print("1 - Vaata punktitabelit")
print("2 - Lisa tulemus")
print("3 - Leia võitude arv")
print("4 - Leia parim")
print("5 - Lõpeta programmi töö")

while True:
    valik = int(input("Sisesta valik: "))
    if valik == 1:
        for nimi in sonastik:
            print(nimi, end=" ")
            for voor in sonastik[nimi]:
                print(voor, end=" ")
            print()
    if valik == 2:
        sonastik = lisa_tulemus(sonastik)
    if valik == 3:
        nimi = str(input("Sisesta riigi nimi: "))
        print(leia_võitude_arv(sonastik,nimi))
    if valik == 4:
        leia_parim(sonastik)
    if valik == 5:
        fail = open("tulemused_uus.txt", "w")
        #voorude_kogus = 0
        indeks = 0
        for nimi in sonastik:
            indeks += 1
            fail.write(nimi+";")
            indeks1 = 0
            for skoor in sonastik[nimi]:
                indeks1 += 1
                if indeks == len(sonastik) and indeks1 == len(sonastik[nimi]):
                    fail.write(skoor)
                elif indeks1 == len(sonastik[nimi]):
                    fail.write(skoor+"\n")
                else:
                    fail.write(skoor+";")

        fail.close()
        print("Faili salvestatud! Progamm lõpetas töö")
        break









