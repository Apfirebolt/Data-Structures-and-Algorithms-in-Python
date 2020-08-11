"""
Tutorial for various operations in dictionary - Python
get, items, update, pop, popitem, keys, values, 
"""

d = {}
s = 'amitprafulla'
for letter in s:
  if letter not in d:
    d[letter] = 1
  else:
    d[letter] += 1

e = {}
r = 'pragatishukla'
for letter in r:
  if letter not in e:
    e[letter] = 1
  else:
    d[letter] += 1

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}
# Sorting a dictionary based on key value.
sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])

print(d)
print(d.values())
print(d.items())
print(d.keys())
print(sorted(d))
print('After updating d older values are replaced with the newer values...')
d.update(e)
print(d)