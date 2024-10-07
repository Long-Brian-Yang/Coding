class Solution:
    def getNext(self, next, s):
        j=-1
        next[0]=j
        for i in range(1,len(s)):
            while j>=0 and s[i]!=s[j+1]:
                j=next[j]
            if s[i]==s[j+1]:
                j+=1
            next[i]=j

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next=[0]*len(needle)
        self.getNext(next,needle)
        j=-1
        for i in range(len(haystack)):
            while j>=0 and haystack[i]!=needle[j+1]:
                j=next[j]
            if haystack[i]==needle[j+1]:
                j+=1
            if j==len(needle)-1:
                return i-j
        return -1

solution = Solution()
haystack1 = "hello"
needle1 = "ll"
output1 = solution.strStr(haystack1, needle1)
print(f"Input: haystack = '{haystack1}', needle = '{needle1}'\nOutput: {output1}") 
