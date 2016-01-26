
num_inputs = 10**5
import numpy as np
from random import randint as ri


def reservoir_sample(buf_size, num_inputs):
    bf = [0] * buf_size
    for i in range(num_inputs):
        if i < buf_size:
            bf[i] = i
        else:
            v = ri(0, i)
            if v < buf_size:
                bf[v] = i

    return np.median(bf)

def root_squared_error(inp):
    true,pred = inp
    return ((true-pred)**2)**.5
true_median =  np.median(xrange(num_inputs))

print true_median
print 'Buffer Size \t Approx Mean \t RSE'
for ii in range(1, 6):
    bf = 10**ii
    approx = []
    for trial in range(5):
        approx += reservoir_sample(bf, num_inputs),
    print '{0} \t {1} \t {2}'.format(bf, np.mean(approx), np.mean(map(root_squared_error, zip([true_median]*(trial+1), approx))))


