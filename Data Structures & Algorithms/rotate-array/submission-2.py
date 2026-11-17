class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        cnt = n
        start = 0
        while cnt > 0:
            idx = start
            saved = nums[idx]
            while True:
                idx += k
                idx %= n
                saved, nums[idx] = nums[idx], saved
                cnt -= 1
                if idx == start:
                    break
            start += 1

        
        


        