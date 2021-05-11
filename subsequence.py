"""
abc
ahbgdcu
"""


def subsequence(f, s):
    f_list = list(f)
    s_list = list(s)

    l, r = 0, 0

    while l < len(f_list) and r < len(s_list):
        if f_list[l] == s_list[r]:
            l += 1
        r += 1
    return l == len(f_list)


if __name__ == '__main__':
    a = input()
    b = input()
    print(subsequence(a, b))
