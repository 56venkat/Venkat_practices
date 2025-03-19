import re
s = "abaabaabaabaaefEAEOUOIouf"
res = re.finditer(r"([bcdfghjklmnpqrstvwxyz])([aeiou]{2,})([bcdfghjklmnpqrstvwxyz])", s, re.IGNORECASE)
print(map(lambda x: x.group(), re.finditer(r"([bcdfghjklmnpqrstvwxyz])([aeiou]{2,})([bcdfghjklmnpqrstvwxyz])", s, re.IGNORECASE)))
'''if res:
    for sub in res:
        for i in sub:
            is_vowel = True
            for j in i:
                if j not in 'aeiouAEIOU':
                    is_vowel = False
                    break
            if is_vowel and i:
                print(i)
else:
    print(-1)'''