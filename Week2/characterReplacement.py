class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length of substring - the number of most frequent element <= k
        count = defaultdict(int)
        maxn = left = right = 0

        while right < len(s):
            count[s[right]] += 1
            maxn = max(maxn, count[s[right]])
            if right - left + 1 - maxn > k:
                count[s[left]] -= 1
                left += 1
            right += 1
        return right - left

    def _characterReplacement(self, s: str, k: int) -> int:
        num=[0] * 26
        maxn = left = right = 0
        n = len(s)
        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        return right - left
