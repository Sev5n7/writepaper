class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char , begin, end = list(s), 0, len(s)-1
        while(begin < end):
            while begin < end and not ('a' <= s[begin] <= 'z' or 'A' <= s[begin] <= 'Z'):
                begin+=1
            while begin < end and not ('a' <= s[end] <= 'z' or 'A' <= s[end] <= 'Z'):
                end-=1
            if begin < end:
                char[begin], char[end] = char[end], char[begin]
                begin+=1
                end-=1
        return ''.join(char)