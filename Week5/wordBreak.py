class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in range(len(s)):
            if s[:i] in wordDict:
                s = s[i:]
        
        if len(s) == 0:
            return True
        return False

    # HashMap   
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.cache = {}
        return self.can_be_break(s, wordDict)
        
    def can_be_break(self, s, wordDict):
        if s in self.cache:
            return self.cache[s]
        
        if not s:
            return True
        
        ans = False
        for word in wordDict:
            # ?k?????
            if s[:len(word)] == word:
                # ??
                if self.can_be_break(s[len(word):], wordDict):
                    ans = True
                    break
        # ??
        self.cache[s] = ans
        
        return ans