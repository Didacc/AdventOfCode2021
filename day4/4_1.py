import sys

# bingo game-like implementation
f = open("data.txt", "r")

lines = f.readlines()

numbers = lines[0].split(',')
i = 2
j = 2
tablesCount = 0
tables = []

while i < 602:
    tablesCount += 1
    while i < j + 5:
        aux = lines[i].strip()
        tables.append(aux.split())
        i += 1
    i += 1
    j += 6



def checkWin():
    i = 0
    sumNotMarked = 0
    while i < tablesCount:
        for y in range(5):
            if tables[i + y][0] == '-1' and tables[i + y][1] == '-1' and tables[i + y][2] == '-1' and tables[i + y][3] == '-1' and tables[i + y][4] == '-1':
                print('row win on table ', i + y, ', row ', y)
                z = i
                for z in range(z, z + 5):
                    for t in range(5):
                        if tables[z][t] != '-1':
                            sumNotMarked += int(tables[z][t])
                return sumNotMarked

            if tables[i][y] == '-1' and tables[i + 1][y] == '-1' and tables[i + 2][y] == '-1' and tables[i + 3][y] == '-1' and tables[i + 4][y] == '-1':
                print('column win on table ', i, ', row ', y)
                z = i
                for z in range(z, z + 5):
                    for t in range(5):
                        if tables[z][t] != '-1':
                            sumNotMarked += int(tables[z][t])
                return sumNotMarked

        i += 5
    return 0


for number in numbers:
    for i in range(len(tables)):
        for j in range(5):
            if tables[i][j] == number:
                tables[i][j] = '-1'
                win = checkWin()
                if win != 0:
                    print('Game over, congrats to the winner, punctuation = ', win * int(number))
                    exit()
