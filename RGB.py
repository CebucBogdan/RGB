from PIL import Image
import numpy as np

""" Am important Image din libraria PIL
    Numpy pentru a putea acea acces la forma de tip array"""
imagine = Image.open('beau.bmp')  # am incarcat poza in memorie(pentru a o putea rula)
img_data = np.array(imagine)  # convertim imaginea intr o matrice de tip numpy
photo_shape = img_data.shape  # photo shape-ul ne indica ca poza are 240 pixeli inaltime, 256 pixeli in latime si are
# 3 tipuri de culori RGB
print(photo_shape)

""" Explicatie: 
        Avem 3 culori RGB, asta inseamna o matrice 3D, imaprita pe 3 canale, 
        pentru a ne asigura ca vedem o singura culoare, trebuie ca 2 dintre cele 3 canele  sa aibe valorile 0
        Canalele sunt luate in functie de ordinea culorilor:
        Red reprezinta canalul 1 (asociat indexului 0)
        Green reprezinta canalul 2 (asociat indexului 1)
        Blue reprezinta canalul 3 (asociat indexului 2)"""

# Vizualizare culoare rosie Rosu
""" In RGB culoarea rosie este pe primul loc, 
    asta inseamna ca o lucram daor cu valorile din primul canal, celelalte 2 raman cu valorile 0"""
img_chn_rosu = np.zeros(img_data.shape, dtype='uint8')  # initializam zerourile ulitizand tip de date
img_chn_rosu[:, :, 0] = img_data[:, :, 0]
imagine_rosu = Image.fromarray(img_chn_rosu)

# Vizualizare culoare rosie Verde
"""La fel si pentru cel de-al 2-lea canal, a 2-a culoare in RGB fiind Green"""
img_chn_verde = np.zeros(img_data.shape, dtype='uint8')
img_chn_verde[:, :, 1] = img_data[:, :, 1]
imagine_verde = Image.fromarray(img_chn_verde)

# Vizualizare culoare rosie Albastru
"""Similar pentru al 3-lea canal, """
img_chn_albastru = np.zeros(img_data.shape, dtype='uint8')
img_chn_albastru[:, :, 2] = img_data[:, :, 2]
imagine_albastru = Image.fromarray(img_chn_albastru)

# Imaginea rasutrnata
""" Prin rasturnarea imaginii intelegem pozitionarea aceteia cu susul in jos, acest lucru se poat face prin dispunerea 
    pozei pe axa 1 Daca o dispuneam pe axa 2, atunci poza aparea intoarsa de la stanga la dreapta Daca incercam pe axa 3 
    atunci se schimba culoarea """
img_rasturnata_data = np.flip(img_data, axis=1)
img_rasturnata = Image.fromarray(img_rasturnata_data)

# Imaginea inversa
""" Valoarea unei matrici este cuprinsa in intervalul [0,255]
    Prin scaderea a fiecare valori din 255 putem afisa poza invers"""
img_inversa_data = 255 - img_data
img_inversa = Image.fromarray(img_inversa_data)

# Imagine rotita
"""Prin intermediul numpy am rotit imaginea la 90 de grade"""
img_rotita_data = np.rot90(
    img_data)  # putem introduce un nou parametru la functia rot pentru o rotire la 270, de exeplu rot90(img_data,3)
img_rotita = Image.fromarray(img_rotita_data)

# Afisare
imagine.show()
imagine_rosu.show()
imagine_verde.show()
imagine_albastru.show()
img_rasturnata.show()
img_inversa.show()
img_rotita.show()
