def main():
    for i in range(20):
        print(fib(30))


def fib(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    main()
