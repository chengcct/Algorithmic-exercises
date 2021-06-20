from collections import defaultdict
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead_set = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ret = []

        def dfs(king):
            if king not in self.dead_set:
                self.ret.append(king)
            for child in self.children[king]:
                dfs(child)

        dfs(self.king)
        return self.ret

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
