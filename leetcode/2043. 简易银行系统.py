# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/18 17:39
"""
输入：
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
输出：
[null, true, true, true, false, false]

解释：
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // 返回 true ，账户 3 的余额是 $20 ，所以可以取款 $10 。
                         // 账户 3 余额为 $20 - $10 = $10 。
bank.transfer(5, 1, 20); // 返回 true ，账户 5 的余额是 $30 ，所以可以转账 $20 。
                         // 账户 5 的余额为 $30 - $20 = $10 ，账户 1 的余额为 $10 + $20 = $30 。
bank.deposit(5, 20);     // 返回 true ，可以向账户 5 存款 $20 。
                         // 账户 5 的余额为 $10 + $20 = $30 。
bank.transfer(3, 4, 15); // 返回 false ，账户 3 的当前余额是 $10 。
                         // 所以无法转账 $15 。
bank.withdraw(10, 50);   // 返回 false ，交易无效，因为账户 10 并不存在。
"""
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.bank = balance
        self.bank_index = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.bank_index or account2 > self.bank_index or self.bank[account1 - 1] < money:
            return False
        self.bank[account1 - 1] -= money
        self.bank[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.bank_index:
            return False
        self.bank[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.bank_index or self.bank[account - 1] < money:
            return False
        self.bank[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
