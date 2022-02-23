func maxSubArray(nums []int) int {
    pre := 0
    ans := -100000
    for _, num := range(nums) {
        pre = max(pre+ num,  num)
        ans = max(pre, ans)

    }
    return ans 
    

}

func max (a,b int ) int {
    if a > b {
        return a
    } 
    return b
}