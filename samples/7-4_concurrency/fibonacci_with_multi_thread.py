from concurrent.futures import ThreadPoolExecutor

calls = []


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    futures = []
    for i in range(20):
        future = executor.submit(fib, 30)
        futures.append(future)

    for future in futures:
        print(future.result())

    print(calls)


def fib(n):
    if n == 30:
        calls.append(n)

    assert n >= 0
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    main()
