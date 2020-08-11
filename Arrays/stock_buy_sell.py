"""Given stock prices for n days, find maximum profit you can make through buy/sell stock in those days"""

prices = list(map(int, input().split(' ')))
max_profit = 0

i = 0
n = len(prices)

while i < n:
    buy_index = i
    while i+1 < n and prices[i+1] > prices[i]:
        i += 1
    sell_index = i
    max_profit += prices[sell_index] - prices[buy_index]
    i += 1
print(max_profit)