if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        print(n)
        r = []
        for i in range(n):
            name, tasks, error = f.readline().strip().split()
            r.append((name, int(tasks), int(error)))
        print(r)
