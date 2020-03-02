import random
from random import randint


class Client:
    def __init__(self, name, passport, money):
        self.name = name
        self.passport = passport
        self.money = money


m1 = ['Валерий', 'Петр', 'Питер', 'Дмитрий', 'Олег', 'Алексей', 'Александр', 'Сергей', 'Захар', 'Юрий']
m2 = [123456, 654321, 567891, 231546, 886950, 786432, 708373, 870347, 909729, 903007]
m3 = [100000, 34567689, 5465756, 4145665, 25626424, 2656255, 2562262, 2526625, 2656256, 265262]


class Thing:
    def __init__(self, name, price):
        self.name = name
        self.price = price


m4 = ['клава', 'мышка', 'кольцо', 'комп', 'браслет', 'пылесос', 'кресло', 'телефон', 'наушники', 'серьги']
m5 = [101, 2002, 30003, 400004, 5352565, 655666, 145411, 2222, 626333, 42464]


class Sdelka:
    def __init__(self):
        self.lmoney = 100000000
        self.things = []

    def zalog(self):
        clients = cl
        things = th
        a = random.choice(clients)
        b = random.choice(things)
        self.lmoney = self.lmoney - b.price
        self.things.append(b.name)
        return self.lmoney, self.things


cl = []
th = []
for i in range(randint(1, 20)):
    a = random.choice(m1)
    b = random.choice(m2)
    c = random.choice(m3)
    d = random.choice(m4)
    e = random.choice(m5)
    cl.append(Client(a, b, c))
    th.append(Thing(d, e))
for i in cl:
    print(i.name, i.passport)
for i in th:
    print(i.name, i.price)
s = Sdelka()
for i in range(len(cl)):
    s.zalog()
print(s.lmoney, s.things)