


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



