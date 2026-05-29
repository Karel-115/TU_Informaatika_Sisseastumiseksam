class Raamat():
    def __init__(self,pealkiri,autor):
        self.pealkiri = pealkiri
        self.autor = autor
        
    def __str__(self):
        return "Raamatu \"" + str(self.pealkiri) + "\" autor on " + str(self.autor)

class Lasteraamat(Raamat):
    def __init__(self, pealkiri,autor, miinimumvanus, maksimumvanus):
        super().__init__(pealkiri,autor)
        self.miinimumvanus = miinimumvanus
        self.maksimumvanus = maksimumvanus
    
    def muuda_soovituslikku_vanust(self,uus_miinimumvanus,uus_maksimumvanus):
        self.miinimumvanus = uus_miinimumvanus
        self.maksimumvanus = uus_maksimumvanus
        print("Soovituslik vanus muudetud!")
        
    def __str__(self):
       return "Lasteraamatu \"" + str(self.pealkiri) + "\" autor on " + str(self.autor)+ ", soovituslik vanus: " + str(self.miinimumvanus) + "-" + str(self.maksimumvanus)
          
raamat = Raamat("Rehepapp","Andrus Kivirähk")
lasteraamat1 = Lasteraamat("Karneval ja kartulisalat","Andrus Kivirähk", 10,12)
lasteraamat2 = Lasteraamat("Sipsik","Eno Raud", 10,12)

print(raamat)
print(lasteraamat1)
print(lasteraamat2)
lasteraamat2.muuda_soovituslikku_vanust(7,9)
print(lasteraamat2)