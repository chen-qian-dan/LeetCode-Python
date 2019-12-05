class Solution1:
    def romanToInt(self, s: str) -> int:
        ret = 0
        coordinates = [("I", 1),
                       ("V", 5),
                       ("X", 10),
                       ("L", 50),
                       ("C", 100),
                       ("D", 500),
                       ("M", 1000),
                       ("IV", 4),
                       ("IX", 9),
                       ("XL", 40),
                       ("XC", 90),
                       ("CD", 400),
                       ("CM", 900)]
        while len(s) > 0:
            if len(s) == 1:
                for item in coordinates:
                    if s == item[0]:
                        ret += item[1]
                        s = ""
            else:
                sub = s[:2]
                is_combined = False
                for item in coordinates:
                    if sub == item[0]:
                        ret += item[1]
                        s = s[2:]
                        is_combined = True
                        break
                if not is_combined:
                    sub = s[0]
                    for item in coordinates:
                        if sub == item[0]:
                            ret += item[1]
                            s = s[1:]
                            break
        return ret
