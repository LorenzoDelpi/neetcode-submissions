class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        for num in nums:
            complementary: int = target - num
            if complementary in nums:
                return [nums.index(num), nums.index(complementary)]