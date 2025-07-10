"""
EXERCIȚII REȚELE NEURONALE - PREDICTIA PREȚULUI MAȘINILOR

Am antrenat o rețea neuronală simplă cu un set mai mare de date despre prețul mașinilor. Rețeaua prezice prețul mașinii pe baza atributelor mașinii. Rețeaua constă dintr-un strat de intrare cu cinci noduri, un strat ascuns cu două noduri, un al doilea strat ascuns cu două noduri, și în final un strat de ieșire cu un singur nod. În plus, există un singur nod bias pentru fiecare strat ascuns și stratul de ieșire.

Programele de mai jos folosesc greutățile acestei rețele antrenate pentru a efectua ceea ce se numește o trecere înainte a rețelei neuronale. Trecerea înainte înseamnă rularea variabilelor de intrare prin rețeaua neuronală pentru a obține ieșirea, în acest caz prețul unei mașini cu atribute date.

EXERCIȚIUL 1 
------------------------------------------------------
Problemele: 
- Nodurile bias nu sunt folosite 
- Funcțiile de activare nu sunt implementate
- Forward pass-ul este incomplet (doar primul strat)

Sarcina: Repară toate problemele de mai sus. Folosește funcția de activare ReLU pentru nodurile ascunse și activare liniară (identitate) pentru nodul de ieșire.

Test: Obține o predicție pentru mașina cu vectorul [74, 5, 10, 2, 100].

EXERCIȚIUL 2 
--------------------------------------------------------------------------
Progres: Bias-urile și funcțiile de activare sunt acum implementate corect.

Problema rămasă: Forward pass-ul este încă incomplet - lipsește al doilea strat ascuns și stratul de ieșire.

Sarcina: Completează implementarea forward pass-ului prin adăugarea straturilor lipsă.

Test: Obține o predicție pentru mașina cu vectorul [82, 2, 65, 3, 516].
"""

import numpy as np

# Greutățile și bias-urile rețelei antrenate
w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
               [-2.75768443e-01,  3.43724167e-01],
               [ 2.29138536e+01,  3.91783025e-01],
               [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
               [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
               [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

# Date de antrenament (pentru referință)
x = np.array([[111, 13, 12, 1, 161],
              [125, 13, 66, 1, 468],
              [46, 6, 127, 2, 961],
              [80, 9, 80, 2, 816],
              [33, 10, 18, 2, 297],
              [85, 9, 111, 3, 601],
              [24, 10, 105, 2, 1072],
              [31, 4, 66, 1, 417],
              [56, 3, 60, 1, 36],
              [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550., 75850.,
              93300., 170650., 149000.])



def activare_ascunsa_ex1(z):
    pass

def activare_iesire_ex1(z):
    pass



x_test_ex1 = [[74, 5, 10, 2, 100]]
for element in x_test_ex1:
    h1_in = np.dot(element, w0)  # îi lipsește termenul bias, repară-l!
    h1_out = activare_ascunsa_ex1(h1_in)  # aplică funcția de activare
    
    # doar primul strat este implementat
    # completează restul forward pass-ului!
    
    print(0)

print("\n")



def activare_ascunsa_ex2(z):
    pass

def activare_iesire_ex2(z):
    pass



x_test_ex2 = [[82, 2, 65, 3, 516]]
for element in x_test_ex2:
    h1_in = np.dot(element, w0) + b0  
    h1_out = activare_ascunsa_ex2(h1_in)  

    
    print(0)  # înlocuiește cu implementarea completă
