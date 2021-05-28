from threading import Semaphore, Lock, Event


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.s = Semaphore(0)
        self.lock = Lock()
        # 初始化两个事件，控制两个事件的有序性，初始时事件是false
        self.event_odd = Event()
        self.event_even = Event()
        # 先发生的是奇数事件
        self.event_odd.set()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            # 获取锁
            self.lock.acquire()
            printNumber(0)
            # 释放一个资源
            self.s.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            # 等待事情发送
            self.event_even.wait()
            # 等待资源
            self.s.acquire()
            printNumber(i)
            # 结束当前事件
            self.event_even.clear()
            # 释放锁
            self.lock.release()
            # 触发另一个事件
            self.event_odd.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            # 等待事件发生
            self.event_odd.wait()
            # 等待资源
            self.s.acquire()
            printNumber(i)
            # 结束当前事件
            self.event_odd.clear()
            # 释放锁
            self.lock.release()
            # 触发另一个事件
            self.event_even.set()


print(ZeroEvenOdd(2))
