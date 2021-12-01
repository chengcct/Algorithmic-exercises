def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = prev + curr, curr


if __name__ == '__main__':
    f = fib()
    for i in range(10):
        print(next(f))