def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return res


f = open('data.txt', 'r')
content = f.readlines()
binary = []
for line in content:
    binary.append(line[:-1])

numberOfOnes = 0
oxygenList = binary[:]
oxygenListAux = binary[:]
co2List = binary[:]
co2ListAux = binary[:]


for i in range(len(binary[0])):
    if len(oxygenListAux) == 1:
        break
    numberOfOnes = 0
    for t in range(len(oxygenListAux)):
        numberOfOnes += int(oxygenListAux[t][i])
    if numberOfOnes >= (len(oxygenListAux) / 2):
        for element in oxygenList:
            if element[i] == '0' and element in oxygenListAux:
                oxygenListAux.remove(element)
    else:
        for element in oxygenList:
            if element[i] == '1' and element in oxygenListAux:
                oxygenListAux.remove(element)

for i in range(len(binary[0])):
    if len(co2ListAux) == 1:
        break
    numberOfOnes = 0
    for t in range(len(co2ListAux)):
        numberOfOnes += int(co2ListAux[t][i])
    if numberOfOnes >= (len(co2ListAux) / 2):
        for element in co2List:
            if element[i] == '1' and element in co2ListAux:
                co2ListAux.remove(element)
    else:
        for element in co2List:
            if element[i] == '0' and element in co2ListAux:
                co2ListAux.remove(element)


stringCo2 = str(convert(co2ListAux))
stringOxygen = str(convert(oxygenListAux))
oxygen = int(stringOxygen, 2)
co2 = int(stringCo2, 2)

print("final result(co2*oxygen): ", oxygen * co2)  # 4201875 > correctAnswer > 684600

f.close()
