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


def combination(numbers: str, s: str, length: int, idx: int) -> str:
    if length == 0:
        print(s, end=' ')
    else:
        for symbol in NUMBERS[numbers[idx]]:
            combination(numbers, s + symbol, length - 1, idx + 1)


if __name__ == '__main__':
    combination('23456', '', len('23456'), 0)
