class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = defaultdict(int), []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            # find one's reverse and they are not the same one
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
            
            # empty string
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
            
            for j in range(len(word)):
                # front part is the reverse of other word, and back part is a palindrome
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res