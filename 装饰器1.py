import time


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print('used:', end - start)

    return wrapper


@timeit
def foo():
    print('done')


if __name__ == '__main__':
    foo()
