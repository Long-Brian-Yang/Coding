class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, 0, 1, [], result)
        return result

    def backtrack(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:
            return
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9-(k-len(path))+2):
            currentSum += i
            path.append(i)
            self.backtrack(targetSum, k, currentSum, i+1, path, result)
            currentSum -= i
            path.pop()