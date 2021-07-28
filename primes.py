from math import sqrt


def fibonacii(n):
    yield 0
    yield 1
    liczba_poprzednia = 0
    liczba = 1
    ilosc_wygenerowanych = 2
    while ilosc_wygenerowanych < n:
        nowa_liczba = liczba + liczba_poprzednia
        liczba_poprzednia = liczba
        liczba = nowa_liczba
        yield nowa_liczba
        ilosc_wygenerowanych += 1


def parzyste(n):
    liczba = 0
    ilosc_wygenerowanych = 0
    while ilosc_wygenerowanych < n:
        liczba += 2
        yield liczba
        ilosc_wygenerowanych += 1


def prime_generator(n):
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


class PrimeIterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()
