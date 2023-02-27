"""
给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：
"""
def movesToMakeZigzag(self, nums: list[int]) -> int:
    ret = [0] * 2
    for index, num in enumerate(nums):
        left = nums[index-1] if index > 0 else float('inf')
        right = nums[index+1] if index < len(nums)-1 else float('inf')
        ret[index % 2] += max(0, num - min(left, right) + 1)
    return min(ret)
