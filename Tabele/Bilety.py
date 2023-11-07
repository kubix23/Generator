import random

from faker import Faker

class Bilety:
    def __init__(self, num, start='-3y', end='-1y'):
        self.faker = Faker('pl_PL')
        self.startTime = start
        self.endTime = end
        self.id = [i for i in range(num)]
        self.dataSprzedazy = [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)]
        temp = [randomCost() for _ in range(num)]
        temp = [(x[0],x[1],x[2]//2 if x[1] else x[2]) for x in temp]
        self.cena = [x[2] for x in temp]
        self.rodzajBiletu = [x[0] for x in temp]
        self.ulga = [x[1] for x in temp]

    def extend(self, num, end='now'):
        for i in range(10):
            self.rodzajBiletu[random.randint(0, len(self.rodzajBiletu)-1)] = random.randint(1, 5)

        self.startTime = self.endTime
        self.endTime = end
        self.id.extend([self.id[-1]+i for i in range(num)])
        self.dataSprzedazy.extend([self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)])
        temp = [randomCost() for _ in range(num)]
        temp = [(x[0],x[1],x[2]//2 if x[1] else x[2]) for x in temp]
        self.cena.extend([x[2] for x in temp])
        self.rodzajBiletu.extend([x[0] for x in temp])
        self.ulga.extend([x[1] for x in temp])

    def save(self, ver = 0):
        with open(f'bilety{ver}.bulk', 'w') as f:
            for i in range(len(self.id)):
                f.write(f"{self.id[i]},{self.dataSprzedazy[i]},{self.cena[i]},{self.rodzajBiletu[i]},{self.ulga[i]}\n")
def randomCost():
    rodzaj_biletu = random.randint(1, 5)
    ulga = random.choice([True, False])
    cena = [8, 15, 30, 40, 200][rodzaj_biletu-1]
    return rodzaj_biletu, ulga, cena
