func reverseOnlyLetters(s string) string {
    bytes := []byte(s)
     
    for l,r := 0, len(s)-1 ; l<r ; {
        for l < r && !((bytes[l] >= 'a' && bytes[l] <= 'z') || (bytes[l] >= 'A' && bytes[l] <= 'Z')) {
            l++
        }
        for l<r && !(( bytes[r] >= 'a' && bytes[r] <= 'z' ) || (bytes[r]  >= 'A' && bytes[r]  <= 'Z' )) {
            r--
        }
        if l<r {
            bytes[l], bytes[r] = bytes[r], bytes[l]
            l++
            r--
        }
    }
    return string(bytes)
}