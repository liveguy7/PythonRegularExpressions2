import re

def textMatch(txt):
    patterns = '^a(b*)$'
    patterns1 = 'ab+?'
    if(re.search(patterns,txt)):
        return True
    else:
        return False

print(textMatch("ab"))
print(textMatch("a"))
print(textMatch("abc"))
print(textMatch("a"))
















