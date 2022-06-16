class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums:
            # nums_checker = []
            # for i in nums:
            #     if i in nums_checker:
            #         return True
            #     else:
            #         nums_checker.append(i)
            # return False
            nums_checker = set(nums)
            if len(nums_checker) < len(nums):
                return True
            else:
                return False
        else:
            print("empty list")
        