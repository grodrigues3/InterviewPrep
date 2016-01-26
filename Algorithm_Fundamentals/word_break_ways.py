import time
txt = 'barstoolbarstool'
txt = 'abarstoolbarstool'
#bar stool bar stool
#bar stool bars tool
#bar stool bars tool
#bars tool bar stool
words = ['a', 'bars', 'tool', 'stool', 'bar']
d = {}
def parse(s):
    n = len(s)
    if n == 0:
        return 1
    c = 0
    for i in range(1,n+1):
        if s[:i] in words:
            if s[i:] not in d:
                d[s[i:]] = parse(s[i:])
            c += d[s[i:]]
            #c+= parse(s[i:])
    return c
s = time.time()
iters = 10**4
for i in range(iters):
    parse(txt)
print d
print parse(txt)
print time.time() - s


