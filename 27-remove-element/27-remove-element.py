class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # final_len = 0
        # for i, j in enumerate(nums):
        #     if j == val:
        #         nums[i] = float('inf')
        #     else:
        #         final_len += 1
        # nums = sorted(nums)
        # # nums = nums[:final_len]
        # print(nums)
        # return final_len
        
        i = 0
        for j in nums:
            if j != val:
                nums[i] = j
                i += 1
        return i
                
        
        
        