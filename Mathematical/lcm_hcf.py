""" Given 2 numbers, print the lowest common multiple and highest common factor """


def euclid(a, b):
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

n1, n2 = map(int, input().split(' '))
if n1 > n2:
    hcf = euclid(n1, n2)
    lcm = (n1 * n2) // hcf
    print(hcf, lcm)
else:
    hcf = euclid(n1, n2)
    lcm = (n1 * n2) // hcf
    print(hcf, lcm)


