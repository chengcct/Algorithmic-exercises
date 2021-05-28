class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.isword = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        res = self
        for i in word:
            if i not in res.child:
                res.child[i] = Trie()
            res = res.child[i]
        res.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        res = self
        for i in word:
            if i not in res.child:
                return False
            res = res.child[i]
        return res.isword == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        res = self
        for i in prefix:
            if i not in res.child:
                return False
            res = res.child[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
