import random
import string

from faker import Faker


class Autobusy:
    def __init__(self, num, start='-3y', end='-1y'):
        self.faker = Faker('pl_PL')
        self.startTime = start
        self.endTime = end
        self.id = [i for i in range(num)]
        self.dataZakupu = [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)]
        self.iloscMiejsc = [random.randint(12, 50) for _ in range(num)]
        self.numerRejestracyjny = [self.faker.unique.license_plate() for i in range(num)]

    def extend(self, num, end='now'):
        for i in range(10):
            self.numerRejestracyjny[random.randint(0,len(self.numerRejestracyjny)-1)] = self.faker.unique.license_plate()

        self.startTime = self.endTime
        self.endTime = end
        self.id.extend([self.id[-1]+i for i in range(num)])
        self.dataZakupu.extend([self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)])
        self.iloscMiejsc.extend([random.randint(12, 50) for _ in range(num)])
        self.numerRejestracyjny.extend([self.faker.unique.license_plate() for i in range(num)])


    def save(self, ver = 0):
        with open(f'autobusy{ver}.bulk', 'w') as f:
            for i in range(len(self.id)):
                f.write(f"{self.id[i]},{self.dataZakupu[i]},{self.iloscMiejsc[i]},{self.numerRejestracyjny[i]}\n")
