
def minPeople(minOdds):
    if minOdds >= 100:
        return 'Impossible'
    DAYS_PER_YEAR = 365
    target = 1 - minOdds / 100.
    number_of_people = 1.
    p = 1
    while (p > target):
        p *= (1. - number_of_people/DAYS_PER_YEAR)
        number_of_people +=1
    return int(number_of_people)



def print_results(odds):
    print minPeople(odds), 'is minimum number of people before having' + \
            ' a greater than', odds, 'chance of two people having same birthday'

for i in range(10,101,10):
    print_results(i)

