class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i in dict_.keys():
                dict_[i] +=1
            else:
                dict_[i]=1
        for i in dict_.keys():
            if dict_[i]>= (len(nums)/2):
                return i
            
        return count
