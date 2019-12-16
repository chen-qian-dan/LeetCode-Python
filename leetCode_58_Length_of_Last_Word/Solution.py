'''
Qian Chen
20191216Mon
'''
class Solution:
    def lengthOfLastWord(self, s: str):
        '''
        :param s:
        :return: int
        '''
        s = s.strip()
        strs = s.split(" ")
        return len(strs[-1])



