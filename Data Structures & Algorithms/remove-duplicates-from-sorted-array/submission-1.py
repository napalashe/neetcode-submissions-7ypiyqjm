class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        k = 0

        # for num in nums:
        #     if num in seen:
        #         nums.remove(num)
        #     seen.append(num)
        # k = len(nums)
        
        # return k
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i -1]:
                nums[l] = nums[i]
                l +=1 
        return l


