import random

from faker import Faker


class Csv:
    def __init__(self, num, punktyTrasy):
        self.faker = Faker('pl_PL')
        self.nazwaMiasta = random.sample(punktyTrasy.miasto, k=num)
        self.liczbaLudnosci = [random.randint(1000, 1000000) for _ in range(num)]
        self.wielkoscMiasta = [random.random() * 20 + 5 for _ in range(num)]
        self.kodPocztowy = [self.faker.postalcode() for _ in range(num)]
        self.biuro = [self.faker.street_address() for _ in range(num)]

    def extend(self, num, punktyTrasy):
        for i in range(10):
            self.liczbaLudnosci[random.randint(0, len(self.liczbaLudnosci)-1)] = random.randint(1000, 1000000)

        self.nazwaMiasta.extend(random.sample(punktyTrasy.miasto, k=num))
        self.liczbaLudnosci.extend([random.randint(1000, 1000000) for _ in range(num)])
        self.wielkoscMiasta.extend([random.random() * 20 + 5 for _ in range(num)])
        self.kodPocztowy.extend([self.faker.postalcode() for _ in range(num)])
        self.biuro.extend([self.faker.street_address() for _ in range(num)])

    def save(self, ver=0):
        with open(f'csv{ver}.csv', 'w') as f:
            for i in range(len(self.nazwaMiasta)):
                f.write(
                    f"{self.nazwaMiasta[i]},{self.liczbaLudnosci[i]},{self.wielkoscMiasta[i]},{self.kodPocztowy[i]},{self.biuro[i]}\n")
