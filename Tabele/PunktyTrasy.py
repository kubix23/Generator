import random

from faker import Faker


class PunktyTrasy:
    def __init__(self, num):
        self.faker = Faker('pl_PL')
        self.id = [i for i in range(num)]
        self.miasto = [self.faker.city() for _ in range(num)]
        self.ulica = [self.faker.street_name() for _ in range(num)]
        self.adres = [self.faker.building_number() for _ in range(num)]

    def extend(self, num):
        for i in range(10):
            self.adres[random.randint(0, len(self.adres)-1)] = self.faker.building_number()

        self.id.extend([self.id[-1] + i for i in range(num)])
        self.miasto.extend([self.faker.city() for _ in range(num)])
        self.ulica.extend([self.faker.street_name() for _ in range(num)])
        self.adres.extend([self.faker.street_address().split(" ")[2] for _ in range(num)])

    def save(self, ver = 0):
        with open(f'punktyTrasy{ver}.bulk', 'w') as f:
            for i in range(len(self.id)):
                f.write(f"{self.id[i]},{self.miasto[i]},{self.ulica[i]},{self.adres[i]}\n")