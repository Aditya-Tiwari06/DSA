class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        for i in range(n):
            if nums[i]<=0:
                nums[i]=1
        for i in range(n):
            val = abs(nums[i])
            if val>=1 and val<=n:
                if nums[val-1]>0:
                    nums[val-1]=-1*(nums[val-1])
                else:
                    continue
        all_p = False
        for i in range(n):
            
            if nums[i] > 0:
                return i+1

            else:
                all_p = True
                continue
        if all_p == True:
            return n+1