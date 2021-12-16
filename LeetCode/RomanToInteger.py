# Given a roman numeral, convert it to an integer.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

from collections import defaultdict


dic: defaultdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
def roman2int(s: str) -> int:
    if not isinstance(s,str):
        raise TypeError
    
    num = []
    for c in s[::-1]:
        if len(num) >= 1:
            if dic[c.upper()] == 1 and num[-1] == 5:
                num[-1] = 4
                continue
            elif dic[c.upper()] == 1 and num[-1] == 10:
                num[-1] = 9
                continue
            elif dic[c.upper()] == 10 and num[-1] == 50:
                num[-1] = 40
                continue
            elif dic[c.upper()] == 10 and num[-1] == 100:
                num[-1] = 90
                continue
            elif dic[c.upper()] == 100 and num[-1] == 500:
                num[-1] = 400
                continue
            elif dic[c.upper()] == 100 and num[-1] == 1000:
                num[-1] = 900
                continue
        num.append(dic[c.upper()])
    return sum(num)
    
print(roman2int("MCMXCIV"))