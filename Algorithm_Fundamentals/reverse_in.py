
def reverse(s):
    s = list(s)

    n = len(s)
    for i in range((n+1)/2):
        s[i],s[n-1-i] = s[n-1-i], s[i]

    return "".join(s)


test = 'hello'
print reverse(test)
