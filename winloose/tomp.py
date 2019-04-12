import sys

def preparewinlossList(possiblekillers):
    winloslist = list()
    bestkiller = dict()
    selected = set()
    print possiblekillers
    for key in possiblekillers:
        for p in sorted(possiblekillers[key], reverse=True):
            if p in selected:
                continue
            bestkiller[key] = p
            selected.add(p)

    print bestkiller
    return False



def getresult(villainstrengths, playerenergies, numofplayers):
    totalplayersenergy = 0
    # for energy in playerenergies:
    #     totalplayersenergy += energy

    # totalvillainstrength = 0
    # for strength in villainstrengths:
    #     totalvillainstrength += strength

    # if totalplayersenergy < totalvillainstrength:
    #     return "LOSE"

    possiblekillers = dict()
    for villain in villainstrengths:
        for player in playerenergies:
            if player > villain:
                if villain in possiblekillers:
                    possiblekillers[villain].append(player)
                else:
                    possiblekillers[villain] = [player]

    if len(possiblekillers) < numofplayers:
        return "LOSE"

    winlostlist = preparewinlossList(possiblekillers)

    # print(possiblekillers)



def main():
    firstpass = 0
    testcases = 0
    numofplayers = 0
    fp = open("input.txt")
    playerenergies = list()
    villainstrengths = list()
    for line in fp:
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

