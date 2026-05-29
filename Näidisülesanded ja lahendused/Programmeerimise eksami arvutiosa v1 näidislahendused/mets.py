def juurdekasv(S,hektar):
    S=S*0.4047
    return round(S*hektar,2)

faili_nimi = input("Sisestage failinimi: ")
kasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

with open(faili_nimi, "r", encoding="UTF-8") as file:
    content = file.read()
    #content = content.split()
    #print(content)
arvutati=0
for S in content:
    #print(float(S))
    if float(S) > piir:
        print("Metsatüki aastane juurdekasv on " + str(juurdekasv(float(S),kasv)))
        arvutati += 1
    else:
        print("Metsatükki ei võeta arvesse")
print("Arvutati " + str(arvutati) + " metsatüki juurdekasv")