import traceback
addition = 0


def add(num):
    global addition
    # print(addition)
    if int(num) < 10:
        # print('num 2 = {}'.format(num))
        addition += num
    else:
        addition += num % 10
        # print('num = {}'.format(num))
        add(int(num/10))

    return addition


def fibonaccis(num):
    # print(num)
    if num <= 1:
        return num

    return fibonaccis(num-1) + fibonaccis(num-2)


def main():
    print('Recursive program to sum all the digits os a number')
    # ret = add(2358)
    # print(ret)
    tmp = fibonaccis(8)
    print(tmp)


if __name__ == '__main__':
    main()