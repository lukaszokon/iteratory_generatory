if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    for index, liczba in enumerate(a):
        print(f'Index: {index}, Wartość: {liczba}')

    a = 'Ala ma kota'
    for litera in a:
        print(litera)

    a = {'imie': 'Adam', 'nazwisko': 'Kowalski', 'wiek': 25}
    for item in a:
        print(item)