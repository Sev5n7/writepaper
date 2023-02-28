"""
输入: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
输出: [[1,6],[3,9],[4,5]]
"""

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        ret = Counter()
        for v,w in items1 + items2:
            ret[v] += w
        
        return sorted(ret.items())

## 其中 items1 + items2 可以用 chain(items1, items2) 代替