def arvuta_hind(aeg,hind):
    if aeg >= 20:
        return 5.15
    else:
        return float(round(aeg*hind,2))
    
hind = float(input("Sisestage minuti hind eurodes: "))
raha_planeeritud = float(input("Kui palju raha on planeeritud? "))

fail = open("min.txt", encoding="UTF-8")
indeks = 0
kokku = 0
for rida in fail:
    indeks += 1
    rida = rida.strip()
    #print(rida)
    rida = int(rida)
    p_hind = arvuta_hind(rida,hind)
    kokku += p_hind
    print(str(indeks) + ". päeval kulus " + str(p_hind) + " eurot.")
print("Kokku kulus raha " + str(round(kokku,2))+ " eurot.")
if kokku > raha_planeeritud:
    print("Eelarve läks lõhki!")
fail.close()