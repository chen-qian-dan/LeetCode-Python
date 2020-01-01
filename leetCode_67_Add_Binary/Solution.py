
class Solution:
    def addBinary(self, a: str, b: str):
        '''
        :param a: str
        :param b: str
        :return: str
        '''

        # binary to digital
        A = 0
        for i in range(len(a)):
            A += pow(2, i) * a[i]
        B = 0
        for i in range(len(b)):
            B += pow(2, i) * b[i]

        C = A + B

        # digital to binary
        ret = ""
        while C >= 2:
            reminder = C % 2
            ret += str(reminder)
            C = int(C / 2)
        ret += str(C)

        return ret
        

