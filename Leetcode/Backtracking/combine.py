from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n+1):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()

# Test case
def test_combine():
    sol =Solution()
    test_case = (4,2)
    expected_output = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4]
    ]
    result = sol.combine(*test_case)
    print("Test case: n={test_case[0]}, k={test_case[1]}")
    print("Expected output:", expected_output)
    print("Actual output:",result)
    assert result == expected_output, "Test failed!"
    print("Test passed!")

test_combine()