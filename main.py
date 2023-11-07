import time
from datetime import datetime

import names
from random import randrange

from Tabele.Autobusy import Autobusy
from Tabele.Bilety import Bilety
from Tabele.Csv import Csv
from Tabele.Kierowcy import Kierowcy
from Tabele.Kursy import Kursy
from Tabele.PunktyTrasy import PunktyTrasy
from Tabele.Skasowanie import Skasowanie

if __name__ == '__main__':
    num1 = 200
    b = Bilety(num1 * 40)
    a = Autobusy(num1)
    ki = Kierowcy(num1)
    pt = PunktyTrasy(num1 * 10)
    ku = Kursy(num1 * 10, a, ki, pt)
    s = Skasowanie(b, ku, a)
    csv = Csv(num1 // 2, pt)
    # --------------------
    b.save()
    a.save()
    ki.save()
    pt.save()
    ku.save()
    s.save()
    csv.save()
    # --------------------
    num2 = 50
    b.extend(num2)
    a.extend(num2)
    ki.extend(num2)
    pt.extend(num2)
    ku.extend(num2, a, ki, pt)
    s.extend(b, ku, a)
    csv.extend(num2 // 2, pt)
    # --------------------
    b.save(1)
    a.save(1)
    ki.save(1)
    pt.save(1)
    ku.save(1)
    s.save(1)
    csv.save(1)
