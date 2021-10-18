#równe
print(5 == 5)
#różne
print(5 != 1)
#mniejsze lub równe
print(5 <= 5)

a = input('Podaj liczbę a: ')
b = input('Podaj liczbę b: ')
if int(a) > int(b):
    print('a Większe b')
elif int(a) < int(b):
    print('a Mniejsze b')
else:
    print('a równe b')