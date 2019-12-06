
'''
Qian Chen
20191206Thu
'''

class Solution1:
    def longestCommonPrefix(self, strs):
        '''
        :param strs: List[str]
        :return: str
        '''
        # find the shortest string in the array
        if len(strs) == 0:
            return ""
        ret = strs[0]
        for str in strs:
            if len(ret) < len(str):
                ret = str
        # check if ret is the longest common prefix,
        # if not, then delete the last letter in ret
        # until ret become empty.
        has_found = False
        while ret:
            if not has_found:
                has_found = True
            else:
                break
            for str in strs:
                if ret != str[:len(ret)]:
                    ret = ret[:-1]  # the same as ret[:len(ret)-1]
                    has_found = False
                    break
        return ret
