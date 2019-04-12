''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

def getresult(villainstrengths, playerenergies, numofplayers):
    print(playerenergies.sum())

def main():
    firstpass = 0
    testcases = 0
    numofplayers = 0
    playerenergies = list()
    villainstrengths = list()
    for line in sys.stdin:
        if firstpass == 0:
            testcases = int(line.rstrip('\n'))
            firstpass += 1
        elif firstpass == 1:
            numofplayers = int(line.rstrip('\n'))
            firstpass += 1
        elif firstpass == 2:
            firstpass += 1
            for i in line.rstrip('\n').split():
                villainstrengths.append(int(i))
        elif firstpass > 2:
            firstpass += 1
            for i in line.rstrip('\n').split():
                playerenergies.append(int(i))

        # print(testcases)
        # print(numofplayers)
        # print(villainstrengths)
        # print(playerenergies)

    res = getresult(villainstrengths, playerenergies, numofplayers)


main()

