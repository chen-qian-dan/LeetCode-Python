
'''
Qian Chen
20191207Sat
'''

class Solution:
    def isValid(self, s):
        '''
        :param s: str
        :return: bool
        '''
        dic = {"(": ")",
               "{": "}",
               "[": "]"}

        left = ["(", "{", "["]
        right = [")", "}", "]"]

        s_left = ""

        if len(s) % 2 != 0:
            return False
        elif not s:
            return True
        elif s[0] in right:
            return False

        for char in s:
            if char in left:
                s_left += char
            elif char in right:
                last_l = s_left[-1]
                if dic.get(last_l) == char:
                    s_left = s_left[:-1]
                else:
                    return False

        if s_left:
            return False
        else:
            return True

