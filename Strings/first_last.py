""" Given a range between M and N, determine how many numbers would be there within this range with same first and 
last digits """

m, n = map(int, input().split(' '))
cnt = 0
for i in range(m, n+1):
    if str(i)[0] == str(i)[len(str(i))-1]:
        cnt += 1
print(cnt)