import numpy as np
import pdb
q = 13
#chars = list('abcdefghij')
chars = list('abcde')
d = len(chars)
pattern = 'abdd'
np.random.seed(4)


test = "".join(np.random.choice(chars, size=10**6, replace=True)) + pattern
test = pattern + 'aaaa' + pattern
#print test
n = len(test)
def rabin_karp():
    p_hash = t_hash = 0
    n_pat = len(pattern)
    for i in range(n_pat):
        p = pattern[i]
        t = test[i]
        ind = chars.index(p)
        p_hash = (d*p_hash + ind +1) % q
        t_hash = (d*t_hash +(chars.index(t)+1) ) % q
    for start in range(n - n_pat+1):
        if start != 0:
            sig_ind = chars.index(test[start-1]) + 1
            t_hash = (d*(t_hash - sig_ind*(d**(n_pat-1))) + chars.index(test[start+n_pat-1]) + 1) % q

        if t_hash == p_hash:
            if test[start:start+n_pat] == pattern:
                print "Found an index at {0}".format(start)
            else:
                print "Spurious hit"
                pdb.set_trace()
            #print test[start:start+n_pat], pattern
        #print t_hash

rabin_karp()

    


