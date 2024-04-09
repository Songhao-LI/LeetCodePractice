class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


class Trie:            
    def __init__(self):
        self.root = {}
 
    def insert(self, word):
        p = self.root
        for c in word:            
            if c not in p: 
                p[c] = {}
            p = p[c]
        p['#'] = True
 
    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:            
            if c not in p:
                return None
            p = p[c]
        return p

