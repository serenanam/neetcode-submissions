class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        currSum = 0
        res = float('-inf')
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            res = max(res, currSum)
        return res

        #Time: O(n)
        #Space: O(1)