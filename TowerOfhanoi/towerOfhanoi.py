def towerOfhanoi(n, source, dest, aux):

    if n == 1:
        print("move disk 1 from {} to {} ".format(source, dest))
        return

    towerOfhanoi(n-1, source, aux, dest)
    print("move disk {} from {} to {}".format(n, source, dest))
    towerOfhanoi(n-1, aux, dest, source)


def main():
    A = str()
    B = str()
    C = str()

    towerOfhanoi(4, A, B, C)

if __name__ == '__main__':
    main()