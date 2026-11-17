class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        preSum = {0: 1}
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k
            res += preSum.get(diff, 0)
            preSum[currSum] = preSum.get(currSum, 0) + 1
        return res
            