class Solution:
    def addDigits(self, num: int) -> int:
        rv = 0
        while len(str(num)) != 1 :
            temp = 0
            for i in str(num):
                temp += int(i)   
            num = temp
        return num


sol = Solution()
print(sol.addDigits(198))