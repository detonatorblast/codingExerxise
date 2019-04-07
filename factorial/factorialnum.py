

def factorialfun(num):
    if num <= 1:
        return num
    return num * factorialfun(num-1)


def main():
    print('recursive function to find factorial of a number\n')
    num = 8
    print(factorialfun(num))


if __name__ == '__main__':
    main()