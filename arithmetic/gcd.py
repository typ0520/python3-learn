def gcd(a, b):
    if a % b == 0:
        return b
    while a != 0:
        a, b = b % a, a
    return b

if __name__ == '__main__':
    print(gcd(1997, 615))
    print(gcd(615, 1997))
    print(gcd(999, 999))
    print(gcd(1680, 640))