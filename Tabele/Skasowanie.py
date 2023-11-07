import random
from datetime import datetime, timedelta

from faker import Faker

from Tabele import Kursy


class Skasowanie:
    def __init__(self, bilety, kursy, autobusy):
        self.faker = Faker('pl_PL')
        self.kursy = []
        self.bilety = []
        self.data = []
        temp = []
        for i in range(len(kursy.id)):
            max_miejsc = autobusy.iloscMiejsc[kursy.autobus[i]]
            kur_start = kursy.pdrk[i]
            filtered_bilety = list(filter(
                lambda x: True if kur_start - timedelta(weeks=4) < bilety.dataSprzedazy[x] < kur_start else False
                , bilety.id
            ))
            zajete_miejsca = random.randint(0, max_miejsc if max_miejsc < len(filtered_bilety) else len(filtered_bilety))
            self.bilety.extend(random.sample(filtered_bilety, k=zajete_miejsca))
            self.kursy.extend([i for _ in range(zajete_miejsca)])
            self.data.extend([self.faker.date_time_between(start_date=kursy.drk[i], end_date=kursy.dzk[i])
                              for _ in range(zajete_miejsca)])

    def extend(self, bilety, kursy, autobusy):
        for i in range(10):
            index = random.randint(0, len(self.data))
            self.data[index] = self.faker.date_time_between(
                start_date=kursy.drk[self.kursy[index]],
                end_date=kursy.dzk[self.kursy[index]]
            )

        temp = []
        for i in range(self.kursy[-1], len(kursy.id)-1):
            max_miejsc = autobusy.iloscMiejsc[kursy.autobus[i]]
            zajete_miejsca = random.randint(1, max_miejsc)
            kur_start = kursy.pdrk[zajete_miejsca]
            filtered_bilety = list(filter(
                lambda x: True if kur_start - timedelta(weeks=10) < bilety.dataSprzedazy[x] < kur_start else False
                , bilety.id
            ))
            self.bilety.extend(random.sample(filtered_bilety, k=zajete_miejsca))
            self.kursy.extend([i for _ in range(zajete_miejsca)])
            self.data.extend([self.faker.date_time_between(start_date=kursy.drk[i], end_date=kursy.dzk[i])
                              for _ in range(zajete_miejsca)])

    def save(self, ver = 0):
        with open(f'skasowanie{ver}.bulk', 'w') as f:
            for i in range(len(self.kursy)):
                f.write(f"{self.kursy[i]},{self.bilety[i]},{self.data[i]}\n")
