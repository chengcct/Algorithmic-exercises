from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += [i]


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


def test5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = Timer('test1()', 'from __main__ import test1')
print('1:', timer1.timeit(1000))

timer2 = Timer('test2()', 'from __main__ import test2')
print('2:', timer2.timeit(1000))

timer3 = Timer('test3()', 'from __main__ import test3')
print('3:', timer3.timeit(1000))

timer4 = Timer('test4()', 'from __main__ import test4')
print('4:', timer4.timeit(1000))

timer5 = Timer('test5   ()', 'from __main__ import test5')
print('5:', timer5.timeit(1000))
