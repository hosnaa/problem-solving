class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]
        
        ## Subtraction
        for i in range(len(nums)):
            required_num = target - nums[i]
            if required_num in nums and nums.index(required_num) != i:
                return [i, nums.index(required_num)]
        