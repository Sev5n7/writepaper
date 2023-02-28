/*
输入: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
输出: [[1,6],[3,9],[4,5]]
*/

package main

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {

	cnt := [1001]int{}
	for _, item := range items1 {
		cnt[item[0]] += item[1]
	}

	for _, item := range items2 {
		cnt[item[0]] += item[1]
	}

	ans := [][]int{}
	for v, w := range cnt {
		if w > 0 {
			ans = append(ans, []int{v, w})
		}
	}
	return ans
}
