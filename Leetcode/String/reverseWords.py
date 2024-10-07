class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.strip()
        s=s[::-1]
        s = ' '.join(word[::-1] for word in s.split())
        return s
    

solution = Solution()

# Test case 1
input_str1 = "Hello World"
output_str1 = solution.reverseWords(input_str1)
print(f"Input: '{input_str1}'\nOutput: '{output_str1}'") 
