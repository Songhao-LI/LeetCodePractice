class Solution:
    def decodeString(self, s: str) -> str:
        num_stk = []
        chr_stk = []
        temp_chr = ""
        temp_num = 0

        for chr in s:
            if chr == '[':
                num_stk.append(temp_num)
                chr_stk.append(temp_chr)
                temp_chr = ""
                temp_num = 0
            elif chr.isdigit():
                temp_num = 10 * temp_num + int(chr)
            elif chr == ']':
                temp_chr = chr_stk.pop() + num_stk.pop() * temp_chr
            else:
                temp_chr += chr
        
        res = "".join(chr_stk) + temp_chr
        return res