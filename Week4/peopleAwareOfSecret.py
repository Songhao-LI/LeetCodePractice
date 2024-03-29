class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        f = [0] * forget
        f[0] = 1

        for day in range(n - 1):
            for i in range(forget - 1, 0, -1):
                # update to next date
                f[i] = f[i - 1]

            new_people = 0
            for i in range(forget):
                if i >= delay:
                    new_people += f[i]
            f[0] = new_people
        
        res = 0
        for people in f:
            res += people
        return res % (10 ** 9 + 7)