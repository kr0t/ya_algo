NUMBERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combo(input_str, answer_str, length, idx):
    if length == 0:
        print(answer_str, end=' ')
    else:
        for i in NUMBERS[input_str[idx]]:
            combo(input_str, answer_str + i, length - 1, idx + 1)


if __name__ == '__main__':
    n = input()
    combo(n, '', len(n), 0)
