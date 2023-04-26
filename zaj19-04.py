#zmienne lokalne - wewnątrz funkcji, nie są do odebranie przez "świat wewnętrzny", nie jest widoczne poza ciałem funkcji
# cokolwiek ~Otylia
#float - tak samo jak int, tylko można dać liczby po przecinku

#7 jest zmienna globalna, a 8 lokalna
# licz=7
# def dzialanie():
#     licz=8
# print(licz)

#tu juz 8 globalnie wywolane
# licz=7
# def dzialanie():
#     licz=8
#     return licz
# licz=dzialanie()
# print(licz)

# def rysujProstokat(d1=3, sz=4, symbol='&'):
#     for i in range(d1):
#         for j in range(sz):
#             print(symbol, end=' ')
#         print()
# rysujProstokat() fajna zmiana


# def silnia(liczba):
#     if liczba==0:
#         return 1
#     else:
#         print(liczba)
#         return liczba * silnia(liczba-1)

# wynik=silnia(4)


 def suma(lista):
     if len(lista)>0:
         print(lista)
         return lista[0]+suma(lista[1:])
     else:
         print(lista) #przydatne żeby widziec co sie jak dzieje
         return 0

listaNew=[1,2,3,4,5]
wynik=suma(listaNew)
print(wynik)

#Zadanie 1
# def dlugosc(lista1):
#     if lista1==[]:
#         print(lista1)
#         return 0
#     else:
#         print(lista1)
#         return 1 + dlugosc(lista1[1:])

# lista11=[1,2,3,4,5]
# wynik=dlugosc(lista11)
# print(wynik)

# def ostatni(lista2):
#     if len(lista2)>0:
#         if len(lista2)==1:
#             return lista2[0]
#         else:
#             print(lista2)
#             return ostatni(lista2[1:])
    
# lista22=[1,2,3,4,5,6]
# wynik=ostatni(lista22).
# print(wynik)


def sum(lista):
    if len(lista)>0:
        return lista[0]+sum(lista[1:])
    else:
        return 0


lista1 = [-1,2,4,1,-8,-16]
print = sum(lista1)
