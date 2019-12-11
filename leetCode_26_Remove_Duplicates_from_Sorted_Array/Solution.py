'''
Qian Chen
20191210Tue
'''
class Solution:
    def removeDuplicates(self, nums):
        '''
        :param nums: List[int]
        :return: List[int]
        '''
        '''
        i = 1
        nCount = len(nums)
        if nCount > 0:
            nCur = nums[0]
        else:
            nCur = 0
        while i < nCount:
            if nums[i] == nCur:
                nums.remove(nums[i])
                nCount = len(nums)
            else:
                nCur = nums[i]
                i += 1
        '''
        for e in nums:
            if nums.count[e] > 1:
                nums.remove(e)
