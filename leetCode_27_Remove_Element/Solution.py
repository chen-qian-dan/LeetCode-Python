'''
Qian Chen
20191211Wed;
'''
class Solution:
    def removeElement(self, nums, val):
        '''
        :param nums:
        :param val:
        :return:
        '''
        i = 0
        nCount = len(nums)
        while i < nCount:
            if nums[i] == val:
                nums.remove(nums[i])
                nCount = len(nums)
            else:
                i += 1