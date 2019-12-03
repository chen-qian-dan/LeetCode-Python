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

