class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp, md = [1] + [0] * (forget - 1), 10 ** 9 + 7
        for i in range(1, n):
            dp[i % forget] = (md + dp[(i + forget - delay) % forget] - dp[i % forget] + (0 if i == 1 else dp[(i - 1) % forget])) % md
        return sum(dp) % md
    