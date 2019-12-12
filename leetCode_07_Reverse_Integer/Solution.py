
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:


        sign = ""
        if x < 0:
            sign = "-"
            x = -1 * x

        # reverse x
        new_x = ""
        for s in str(x):
            new_x = s + new_x
        new_x = sign + new_x

        new_x = int(new_x)
        if new_x > pow(2, 31) - 1 or new_x < -1*pow(2, 31):
            return 0
        else:
            return new_x



