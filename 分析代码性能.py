import random
import cProfile

x = [random.random() for i in range(100000)]


def f1(x):
    l1 = sorted(x)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]


def f2(x):
    l1 = [i for i in x if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]


cProfile.run('f1(x)')
cProfile.run('f2(x)')
