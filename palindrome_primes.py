from math import floor


def is_palindrome(num):
    s = str(num)
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return s[:mid] == s[mid:][::-1]
    else:
        mid = floor(len(s) / 2)
        return s[:mid] == s[mid + 1:][::-1]


def is_prime(num, cache=None):
    if cache is None:
        cache = {}

    if num in cache:
        return cache.get(num)

    if num <= 1:
        return False

    possible_divisors = list(range(2, int(num / 2)))[::-1]
    for t in possible_divisors:
        if num % t == 0:
            return False

    return True


if __name__ == '__main__':
    cache = {}
    for i in range(2, 1000):
        temp = cache[i] = is_prime(i, cache)
        if is_palindrome(i) and temp:
            print(i)
