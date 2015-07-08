"""
A commonly asked probability question that tends to suprise people:
    What is the smallest number of people that get together before
    the chance of two of them having the same birthday is greater 
    than 50%?

Many people are surprised to find that the number is only 23

"""
def minPeople(minOdds):
    if minOdds >= 100:
        return 'Impossible', 1
    DAYS_PER_YEAR = 365
    target = 1 - minOdds / 100.
    number_of_people = 1.
    probability_all_different = 1
    while (probability_all_different > target):
        probability_all_different *= (1. - number_of_people/DAYS_PER_YEAR)
        number_of_people +=1
    return int(number_of_people), (1-probability_all_different)



def print_results(odds):
    ppl, prob = minPeople(odds)
    print ppl, 'is minimum number of people before having' + \
            ' a greater than', odds, 'chance of two people having same birthday'
    print '\t The probabiliity that in a room of {0} people, two them share the same birthday is {1:.3f}'.format(ppl,prob)

for i in range(10,91,10):
    print_results(i)

