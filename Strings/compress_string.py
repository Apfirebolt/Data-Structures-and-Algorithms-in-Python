"""Given a string in form of aabbbcc, compress it like a2b3c2"""

s = input()
i = 0
n = len(s)
cnt = 1
ans = ''
while i < len(s)-1:
    if s[i] == s[i+1]:
        while s[i] == s[i+1]:
            cnt += 1
            i+=1
            if i == n-1:
                break
    else:
        temp = str(s[i]) + str(cnt)
        ans += temp
        cnt = 1
        i += 1
temp = str(s[n-1] + str(cnt))
ans += temp
print(ans)