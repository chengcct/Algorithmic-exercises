class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []
        while 1:
            dominoes = dominoes.replace('R.L', 'R*L').replace('R.', 'RR').replace('.L', 'LL')
            res.append(dominoes)
            print(dominoes)
            if res.count(dominoes) >= 2:
                break
        return dominoes.replace('*', '.')


if __name__ == '__main__':
    Solution().pushDominoes('.L.R...LR..L..')
