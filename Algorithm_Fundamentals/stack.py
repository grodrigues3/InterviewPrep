

def sell_dates(prices):
    stack = []
    iterate = [y for y in enumerate(prices)]
    for thing in reversed(iterate):
        if not stack:
            stack.append(thing)
        elif thing[1] > stack[-1][1]:
            if thing[0] == stack[-1][0] -1:
                stack.pop()
            stack.append(thing)
    return stack
def maxProfit(prices):
    stack = sell_dates(prices)
    purchased = 0
    cost = 0
    maxProfit = 0
    for day, price in enumerate(prices):
        if not stack:
            break
        if day == stack[-1][0]:
            d, sell_price = stack.pop()
            maxProfit += sell_price*purchased - cost
            purchased = cost = 0
        else:
            cost += price
            purchased +=1

    return maxProfit

# 45 - 6 + (8-4) = 43
x = []
x += ([1,2,3,15,4,8], 43),
x += ([1,2,3,15,8], 39),
x+= (range(10, -1, -1), 0),
x+= (range(1,6), 10),

def testBed(testCase, expectedVal):
    calculated = maxProfit(testCase)
    print calculated
    assert calculated == expectedVal

for test, val in x:
    testBed(test, val)

