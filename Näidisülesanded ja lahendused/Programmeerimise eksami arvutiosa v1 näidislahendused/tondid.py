class Tont:
    def __init__(self,nimi,vanus,elukoht):
        self.nimi = str(nimi)
        self.vanus = int(vanus)
        self.elukoht = str(elukoht)
        
    def kummita(self):
        print(str(self.nimi) + " kummitab elukohas " + str(self.elukoht) + "!")
        
    def __str__(self):
        return "Nimi: " + str(self.nimi) + ", vanus: " + str(self.vanus) + ", elukoht: " + str(self.elukoht)

class Võlur(Tont):
    def nõiu(self, isend):
        print(str(self.nimi) + " pani nõiduse, millega sai pihta " + str(isend))

tont = Tont("Nobert",31,"Tartu")
volur1 = Võlur("Harry",17,"Tartu")
volur2 = Võlur("Snape",35,"Tartu")

print(tont)
tont.kummita()
print(volur1)
print(volur2)
volur1.nõiu("Snape")