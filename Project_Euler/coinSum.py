
target = 200

ways = [0] * (target+1)
ways[0] = 1

coins = [1,2,5,10,20,50,100,200]

for coin in coins:
    for i in range(target+1):
        if i >= coin:
            ways[i] += ways[i - coin]

print ways[-1]

