import random
from datetime import timedelta

from faker import Faker


class Kursy:
    def __init__(self, num, autobusy, kierowcy, punktKoncowy, start='-3y', end='-1y'):
        self.faker = Faker('pl_PL')
        self.startTime = start
        self.endTime = end
        self.id = [i for i in range(num)]
        self.drk = [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)]
        self.dzk = [i + timedelta(hours=(random.random() * 10 + 1)) for i in self.drk]
        self.pdrk = [i + timedelta(minutes=random.randint(-10, 10)) for i in self.drk]
        self.pdzk = [i + timedelta(minutes=random.randint(-10, 10)) for i in self.dzk]
        self.dlugoscTrasy = [((self.dzk[i] - self.drk[i]).seconds // 3600) * (60 + random.randint(-4, 10))
                             for i in range(num)]

        self.autobus = list(autobusy.id)
        random.shuffle(self.autobus)
        if num < len(self.autobus):
            self.autobus = self.autobus[:num]
        else:
            for _ in range(num - len(self.autobus)):
                self.autobus.append(random.choice(autobusy.id))

        self.kierowcy = list(kierowcy.id)
        random.shuffle(self.kierowcy)
        if num < len(self.kierowcy):
            self.kierowcy = self.kierowcy[:num]
        else:
            for _ in range(num - len(self.kierowcy)):
                self.kierowcy.append(random.choice(kierowcy.id))

        self.punktPoczatkowy = list(punktKoncowy.id)
        random.shuffle(self.punktPoczatkowy)
        if num < len(self.punktPoczatkowy):
            self.punktPoczatkowy = self.punktPoczatkowy[:num]
        else:
            for _ in range(num - len(self.punktPoczatkowy)):
                self.punktPoczatkowy.append(random.choice(punktKoncowy.id))

        self.punktKoncowy = list(punktKoncowy.id)
        random.shuffle(self.punktKoncowy)
        if num < len(self.punktKoncowy):
            self.punktKoncowy = self.punktKoncowy[:num]
        else:
            for _ in range(num - len(self.punktKoncowy)):
                self.punktKoncowy.append(random.choice(punktKoncowy.id))

        for i in range(num):
            while self.punktKoncowy[i] == self.punktPoczatkowy[i]:
                self.punktKoncowy[i] = random.choice(punktKoncowy.id)

    def extend(self, num, autobusy, kierowcy, punktKoncowy, end='now'):
        for i in range(10):
            self.kierowcy[random.randint(0, len(self.kierowcy)-1)] = random.choice(kierowcy.id)

        self.startTime = self.endTime
        self.endTime = end
        self.id.extend([self.id[-1] + i for i in range(num)])
        temp = [self.faker.date_time_between(start_date=self.startTime, end_date=self.endTime) for _ in range(num)]
        self.drk.extend(temp)
        self.dzk.extend([i + timedelta(hours=(random.random() * 10 + 1)) for i in temp])
        self.pdrk.extend([i + timedelta(minutes=random.randint(-10, 10)) for i in temp])
        self.pdzk.extend([i + timedelta(minutes=random.randint(-10, 10)) for i in temp])
        self.dlugoscTrasy.extend([((self.dzk[i] - self.drk[i]).seconds // 3600) * (60 + random.randint(-4, 10))
                                  for i in range(num)])

        temp = list(autobusy.id)
        random.shuffle(temp)
        if num < len(self.autobus):
            temp = temp[num:]
        else:
            temp.extend(random.choices(autobusy.id, k=num - len(temp)))
        self.autobus.extend(temp)

        temp = list(kierowcy.id)
        random.shuffle(temp)
        if num < len(self.kierowcy):
            temp = temp[num:]
        else:
            temp.extend(random.choices(kierowcy.id, k=num - len(temp)))
        self.kierowcy.extend(temp)

        temp = list(punktKoncowy.id)
        random.shuffle(temp)
        if num < len(temp):
            temp = temp[num:]
        else:
            temp.extend(random.choices(punktKoncowy.id, k=num - len(temp)))
        self.punktPoczatkowy.extend(temp)

        temp = list(punktKoncowy.id)
        random.shuffle(temp)
        if num < len(temp):
            temp = temp[num:]
        else:
            temp.extend(random.choices(punktKoncowy.id, k=num - len(temp)))
        self.punktKoncowy.extend(temp)

        for i in range(num):
            while self.punktKoncowy[i] == self.punktPoczatkowy[i]:
                self.punktKoncowy[i] = random.choice(punktKoncowy.id)

    def save(self, ver = 0):
        with open(f'kursy{ver}.bulk', 'w') as f:
            for i in range(len(self.id)):
                f.write(
                    f"{self.id[i]},{self.drk[i]},{self.dzk[i]},{self.pdrk[i]},{self.pdzk[i]},{self.dlugoscTrasy[i]},{self.autobus[i]},{self.kierowcy[i]},{self.punktPoczatkowy[i]},{self.punktKoncowy[i]}\n")
