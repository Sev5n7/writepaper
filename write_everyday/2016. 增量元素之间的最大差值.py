### 两次for 循环
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (diff := nums[j] - nums[i]) >0:

                    ans = max(ans,diff)
        return ans
            