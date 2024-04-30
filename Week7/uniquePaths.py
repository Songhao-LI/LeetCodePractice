class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom additional row of all the ones
        oldrow = [1]*n
        for i in range(m-1):
            #for each row we are calculating newrow
            newrow = [1]*n
            #traverse through columns in reverse order excluding last column 
            for j in range(n-2, -1, -1):
                #at each postion 'i' answer is answer at 'i+1' block of same row + answer
                #at ith position of bottom row 
                newrow[j] = newrow[j+1] + oldrow[j]
            oldrow = newrow
        return oldrow[0]
        