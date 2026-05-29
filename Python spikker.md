# Materjalid
- W3School - https://www.w3schools.com/python/default.asp - õppida ja infot otsida
- Programmeerimine 1 - https://web.htk.tlu.ee/digitaru/programmeerimine/part/sissejuhatus/ - Eesti keeles dokumentatsioon
- Programmeerimine 2 - https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/pysimplegui-joonistamine/ - Eesti keeles dokumentatsioon
- Python docs - https://www.python.org
- Andmestruktuuride võrdlustabel - https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/andmestruktuuride-vordlustabel/
# randint
```python
from random import randint
print(randint(3, 9)) # Returns a random number between 3 and 9 (both included)
```
# Sõne
Sõne elemente ei saa muuta ega sinna juurde lisada!
Teine variant on märkida sõne sisus olevad probleemsed ülakomad ja jutumärgid langkriipsuga. Sellisel juhul ei loe Python neid sõne piiritlejatena:
```python
print("Jack vastas: \"Rock 'n' roll\".") # Jack vastas: "Rock 'n' roll".
print('Jack vastas: "Rock \'n\' roll".') # Jack vastas: "Rock 'n' roll".
```
Pane tähele, et langkriips \ ja kaldkriips / on erinevad märgid.
Langkriipsu saab kasutada ka teiste erisümbolite rakendamiseks. Näiteks saab reavahetuse lisada kombinatsiooniga \n.
```python
print("Seda kuupaistet!\nOh muutuksin sündides\nmänniks mäetipul!\n-Ryota")
# Seda kuupaistet!
# Oh muutuksin sündides
# männiks mäetipul!
# -Ryota
```
Kui me soovime langkriipsu ennast sõnes kasutada, tuleb see märgistada teise langkriipsuga.
```python
print("Seda kuupaistet!\nOh muutuksin sündides\nmänniks mäetipul!\n-Ryota") # C:\kaustanimi\failinimi.txt
```
Kui tekst on pikk ja seal on palju jutumärke, ülakomasid või reavahetusi, siis on nende käsitsi märkimine tülikas ülesanne. Pythonis on lubatud sõne piirid märkida kolmekordsete jutumärkide või ülakomadega, siis säilivad tekstis sisalduvad jutumärgid, ülakomad ja reavahetused.
```python
print("""Jack vastas: "Rock 'n' roll".""")
print('''Jack vastas: "Rock 'n' roll".''')

print("""Seda kuupaistet!
Oh muutuksin sündides
männiks mäetipul!
--Ryota""")

print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")
```
Kõikide Pythoni sisseehitatud sõnemeetodite juhend asub aadressil http://docs.python.org/3/library/stdtypes.html#string-methods
# Järjend
## viilutamine
```python
a = ['A', 'B', 'C', 'D', 'E']
print(a[0:2]) # ['A', 'B']
print(a[:2]) # ['A', 'B']
print(a[2:5]) # ['C', 'D', 'E']
print(a[2:]) # ['C', 'D', 'E']
print(a[-2:]) # ['D', 'E']
# Järjend[element kust algab kopeerima : element kust lõpetab(ei võta kaasa)]
```
## veel operatsioone
|Avaldis|Väärtus|Kommentaar|
|---|---|---|
|len([2, 1, 4, 3, -5])|5|Elementide arv|
|min([2, 1, 4, 3])|1|Minimaalne element|
|max([2, 1, 4, 3])|4|Maksimaalne element|
|sum([2, 1, 4, 3])|10|Elementide summa|
|sorted([2, 1, 4, 3])|[1, 2, 3, 4]|Tagastab järjestatud järjendi|
|3 in [2, 1, 4, 3]|True|Kas esineb selline element?|
|[2, 1] + [3, 1]|[2, 1, 3, 1]|Järjendite liitmine|
|[2, 1, 4, 1].count(1)|2|Elemendi esinemiste arv|
|[1, 2, 3] == [2, 1, 3]|False|Järjekord on oluline|
## join()
```python
', '.join(['apple', 'banana', 'cherry']) # 'apple, banana, cherry'
' '.join(['Hello', 'world!']) # 'Hello world!'
'-'.join(['2023', '05', '26']) # '2023-05-26'
''.join(['p', 'y', 't', 'h', 'o', 'n']) # 'python'
```
## append
```python
a = [5, 8]
a.append(7)
print(a) # [5, 8, 7]
b = [5, 8]
b += [7]
print(b) # [5, 8, 7]
```
## Iterating
```python
for key, value in my_dict.items(): # iterate through both keys and values
	print(key, value)
for key in my_dict.keys():  # For only keys (can also omit .keys())
	print(key)
for value in my_dict.values(): # For only values
    print(value)
```
# For-tsükkel in range
Viimane element pole kaasa arvatud!
```python
for i in range(4):
    print(i) # 0,1,2,3
for i in range(1, 4):
    print(i) # 1,2,3
for i in range(0, 13, 2): # 2 on samm(võib olla ka negatiivne)
	print(i) # 0,2,4,6,8,10,12
```
# Failist lugemine
txt - https://web.htk.tlu.ee/digitaru/programmeerimine/chapter/lugemine-failist/
csv - https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/csv/
```python
fail = open("andmed.txt", encoding="UTF-8")
for rida in fail:
    print("Lugesin sellise rea: " + rida)
fail.close() # oluline
```
Instead of manually closing files, we can use the with statement. It ensures the file is automatically closed when the block ends.
This code opens the file, reads its contents and automatically closes it after use.
```python
with open("tekst.txt", "r", encoding="UTF-8") as file: # r - read, w - write
    content = file.read()
    print(content)
```
rida.strip() Removes any leading or trailing whitespace, including newline characters.
rida.split() jaotada sõnad järjendisse
rida.split(';') jaotada semikooloni kohalt
# Rekursioon
```python
def faktoriaal(n):
    if n == 0:             # Rekursiooni baas
        return 1
    else:                  # Rekursiooni samm
        return n * faktoriaal(n-1)
print(faktoriaal(4)) # 24
```
# Print on same line
```python
print("a", end="")
print("b")
print("c ")
# ab
# c

tabel = [ [1, 2, 4], [1, 5, 0] ]
for rida in tabel:
    for element in rida:
        print(element, end=" ")
    print()
# 1 2 4 
# 1 5 0
```
# Erindid
```python
arv1 = 10
arv2 = 5
print(f"Nende arvude jagatis on {arv1 / arv2}") # Nende arvude jagatis on 2.0
```
# Maatriks
```python 
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(A[0][0])  # Väljastab 1
print(A[1][1])  # Väljastab 5
print(A[2][2])  # Väljastab 9
```
Kõrvaldiagonaaliks nimetame analoogiliselt järjendit paremalt ülevalt vasakule alla jooksva diagonaali elementidega.
Peadiagonaaliks nimetame järjendit, mis sisaldab kõiki elemente maatriksi diagonaalilt, mis jookseb vasakust ülemisest nurgast paremasse alumisse nurka
# Ennik
https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/lisalugemine-ennik/
```python
def suurim_korrutis(lst1, lst2):
    suurimad = (0, 0)
    for el1 in lst1:
        for el2 in lst2:
            if el1 * el2 > suurimad[0] * suurimad[1]:
                suurimad = (el1, el2) # ennik
    return suurimad
```
# Hulk
https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/lisalugemine-hulk/
```python
h1 = {8, 2, 3, 6, 7}
h2 = set([6, 4, 5])
h3 = set('Tere hommikust')
```
Hulk ei ole järjestatud, hulgas ei ole korduvaid elemente, hulgad on muudetavad.
# OOP paradigma
- Objektid ja klassid - https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/objektid-ja-klassid/
- Slaidid - https://pydoc.pages.taltech.ee/slides/oop/#1
- W3School - https://www.w3schools.com/python/python_classes.asp
- GeeksforGeeks - https://www.geeksforgeeks.org/python/python-classes-and-objects/

- Kapseldamine (encapsulation) - funktsionaalsus peidetakse
- Modulaarsus (modularity) - programm jagatakse iseseisvateks tükkideks
- Polümorfism (polymorphism) - alamklass saab meetodeid üle kirjutada
- Pärimine (inheritance) - alamklass pärib omadused ja meetodid
