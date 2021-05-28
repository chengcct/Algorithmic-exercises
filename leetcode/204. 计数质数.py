class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1] * n
        # 设置0和1位为0
        primes[0] = primes[1] = 0
        # 在2到根号n的范围内，当一个数是质数时，将它所有比n小的倍数设置成0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == 1:
                # 切片，太妙了
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])
        # 现在每个质数位的flag为1，其余的位数为0.由于我们不需要知道质数是什么只要总数，因此直接返回list里面所有1的和就行。
        return sum(primes)


ret = Solution()
print(ret.countPrimes(10))
