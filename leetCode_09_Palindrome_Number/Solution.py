'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s_forward = str(x)
        s_backward = ""
        for s in s_forward:
            s_backward = s + s_backward

        if s_forward == s_backward:
            return True
        else:
            return False

