// 1
func addDigits(num int) int {
    for num > 9 {
        ans:= 0
        for ; num!=0 ; num /= 10 {
            ans+= num%10
        }
        num = ans
    }
    return num

}
// 2 
func addDigits(num int) int {
    if num == 0 {
        return 0
    }
    return (num -1) % 9 + 1

}