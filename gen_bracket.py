def gen_bracket(n, s='', left=0, right=0):
    if left == n and right == n:
        print(s)
    if left < n:
        gen_bracket(n, s + '(', left + 1, right)
    if right < left:
        gen_bracket(n, s + ')', left, right + 1)


if __name__ == '__main__':
    n = int(input())
    gen_bracket(n)
