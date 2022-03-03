# 1
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        while (num > 9 ):
            ans = 0 
            while (num !=0):
                ans += num % 10
                num //= 10
            num = ans
        return ans 
#2 数学法：数根
class Solution:
    def addDigits(self, num: int) -> int:
        return (num -1) % 9 + 1 if num else num




