"""
Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

Constraints:

    Can we assume the string is ASCII?
        Yes
        Note: Unicode strings could require special handling depending on your language
    Is this case sensitive?
        Yes
    Can we use additional data structures?
        Yes
    Can we assume this fits in memory?
        Yes
"""

def compress(string):
        if string is None:
            return None
        elif len(string) <= 1:
            return string

        compstr = [string[0]]
        compstr.append(1)

        for ch in string[1:]:
            if ch == compstr[len(compstr)-2]:
                compstr[len(compstr)-1] += 1
            else:
                if compstr[len(compstr)-1] == 1:
                    compstr.pop(len(compstr)-1)
                compstr.append(ch)
                compstr.append(1)

        if compstr[len(compstr)-1] == 1:
            compstr.pop(len(compstr)-1)

        compstr = ''.join([str(x) for x in compstr])
        # lambda equivalent to above expression
        # compstr = ''.join(map(lambda x:str(x), compstr))
        if len(compstr) < len(string):
            return compstr
        else:
            return string