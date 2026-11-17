class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):
            hashed[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in hashed and i != hashed[target - nums[i]]:
                return [i, hashed[target - nums[i]]]
        
        # Time: O(n)
        # Space: O(n)
