import random
import string

from faker import Faker
import names


class Kierowcy:
    def __init__(self, num, start='-3y', end='-1y'):
        self.faker = Faker('pl_PL')
        self.startTime = start
        self.endTime = end
        self.id = [i for i in range(num)]
        self.imie = [self.faker.first_name() for _ in range(num)]
        self.nazwisko = [self.faker.last_name() for _ in range(num)]
        self.numerPrawojazdy = [numerP() for _ in range(num)]
        self.numerDowodu = [self.faker.unique.identity_card_number() for _ in range(num)]
        self.dataZatrudnienia = [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in
                                 range(num)]
        self.miasto = [self.faker.city() for _ in range(num)]
        self.zarobki = [random.randint(2000, 9000) for _ in range(num)]

    def extend(self, num, end='now'):
        for i in range(10):
            self.numerDowodu[random.randint(0, len(self.numerDowodu)-1)] = self.faker.unique.identity_card_number()

        self.startTime = self.endTime
        self.endTime = end
        self.id.extend([self.id[-1] + i for i in range(num)])
        self.imie.extend([self.faker.first_name() for _ in range(num)])
        self.nazwisko.extend([self.faker.last_name() for _ in range(num)])
        self.numerPrawojazdy.extend([numerP() for _ in range(num)])
        self.numerDowodu.extend([self.faker.unique.identity_card_number() for _ in range(num)])
        self.dataZatrudnienia.extend(
            [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in
             range(num)])
        self.miasto.extend([self.faker.city() for _ in range(num)])
        self.zarobki.extend([random.randint(2000, 9000) for _ in range(num)])

    def save(self, ver = 0):
        with open(f'kierowcy{ver}.bulk', 'w') as f:
            for i in range(len(self.id)):
                f.write(
                    f"{self.id[i]},{self.imie[i]},{self.nazwisko[i]},{self.numerPrawojazdy[i]},{self.numerDowodu[i]},{self.dataZatrudnienia[i]},{self.miasto[i]},{self.zarobki[i]}\n")


def numerP():
    a = f"{random.randint(1, 99999):0>5}"
    b = f"{random.randint(1, 99):0>2}"
    c = f"{random.randint(1, 9999):0>4}"
    return a + "/" + b + "/" + c
