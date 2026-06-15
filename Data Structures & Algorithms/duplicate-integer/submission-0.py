class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_encountered: dict[int, int] = {}

        for num in nums:
            if not (we_already_see_it := nums_encountered.get(num)):
                nums_encountered[num] = 1;
            else:
               return True;

        return False


        