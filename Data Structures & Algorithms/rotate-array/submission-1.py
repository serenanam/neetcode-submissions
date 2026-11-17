class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse array
        l, r = 0, len(nums) - 1
        k %= len(nums)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
       
        # split at k and reverse the two sections
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        