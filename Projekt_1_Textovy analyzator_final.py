'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''' ,
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

hlavicka = '''
Textovy analyzátor: první projekt do Engeto Online Python Akademie

author: Milan Kročil
email: milan.krocil@email.cz
'''
oddelovac = ('-' * 79)
jmeno = input('Zadej prihlasovaci jmeno: ')
heslo = input('Zadej heslo: ')
registrovani_uzivatele = {
    'bob': '123',
    'ann':'pass123',
    'mike':'password123',
    'liz':'pass123'
    }

print(hlavicka, oddelovac)
print('username:', jmeno)
print('password:', heslo)

         
if not jmeno in registrovani_uzivatele or registrovani_uzivatele [jmeno] != heslo:
  print('unregistred user, terminating the program..')
  exit()
else:
  print(oddelovac)
  print('Welcome to the app, ', jmeno) 
  print('We have 3 texts to be analyzed')
  print(oddelovac)

vyber_textu = input('Enter a number btw. 1 and 3 to select: ')
print(oddelovac)
limit=3
if not vyber_textu.isnumeric():                                                 
  print('Nebylo zadano cislo textu. Program ukoncuji...')
  exit()
if not int(vyber_textu) in range(1,limit+1):                                     
  print('Nebyl vybran spravne cislo textu. Program ukoncuji...')
  exit()

texty = {
   '1' : TEXTS [0],
   '2' : TEXTS [1],
   '3' : TEXTS [2]
}
vybrany_text = texty [vyber_textu]

osetreny_text = []
for ocisteni in vybrany_text.split():
   ocistene_slovo = ocisteni.strip('.,!-:')
   osetreny_text.append(ocistene_slovo)

list_pocet_cisel = []
list_pocet_slov_zacinajicich = []
list_pocet_slov_velkymi_pismeny = []
list_pocet_slov_malymi_pismeny = []
sum_cisel = 0

for cisla in osetreny_text:
  if cisla.isnumeric():
    list_pocet_cisel.append(cisla)
    sum_cisel = sum_cisel + int(cisla)
  elif cisla.isupper() and cisla.isalpha():
    list_pocet_slov_velkymi_pismeny.append(cisla)
  elif cisla.islower():
    list_pocet_slov_malymi_pismeny.append(cisla) 
  elif cisla.capitalize():
    list_pocet_slov_zacinajicich.append(cisla) 
 
pocet_cisel = len(list_pocet_cisel)
uppercase = len(list_pocet_slov_velkymi_pismeny)
lowercase = len(list_pocet_slov_malymi_pismeny)
titlecase = len(list_pocet_slov_zacinajicich) 
celkovy_pocet_slov = len(osetreny_text)

print('There are ', celkovy_pocet_slov, 'words in the selected text.')
print('There are ', titlecase, 'titlecase words.')
print('There are ', uppercase, 'uppercase words.')
print('There are ', lowercase, 'lowercase words.')
print('There are ', pocet_cisel, 'numeric strings.') 
print('The sum of all the numbers ', sum_cisel)
print(oddelovac)

pridana_delka = []
serazeny_seznam = sorted(osetreny_text, key = len)
for delka_hodnoty in serazeny_seznam:
  pridana_delka.append(len(delka_hodnoty))

from collections import Counter

cetnost = (Counter(pridana_delka))
print(f"{'LEN':3}|{'OCCURENCES': ^18}|{'NR.'}")
print(oddelovac)
for key, value in cetnost.items():
   print(f"{key:3}|{'*' * int(value):18}|{value}", sep="\n")


