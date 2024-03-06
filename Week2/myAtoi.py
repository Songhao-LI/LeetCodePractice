class Solution:
    def myAtoi(self, s: str) -> int:
        status = 0
        res = 0
        begin = False

        for chr in s:
            if chr == " ":
                if begin == True or status != 0:
                    break
                continue
            if chr == "." or ord('a') <= ord(chr) <= ord('z') or ord('A') <= ord(chr) <= ord("Z"):
                break
            if chr == "+":
                if begin == True or status != 0:
                    break
                status = 1
            if chr == "-":
                if begin == True or status != 0:
                    break
                status = -1
            if chr.isdigit():
                begin = True
                cur_num = int(chr)
                if status == -1:
                    res = res * 10 + status * cur_num
                else:
                    res = res * 10 + cur_num
        
        res = min(res, pow(2, 31) - 1)
        res = max(res, -(2 ** 31))
        return res