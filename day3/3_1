
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
quantity = [0] * (len(str(binary[0])))

for i in range(len(binary)):
    for j in range(len(str(binary[i]))):
        quantity[j] += int(binary[i][j])

for i in range(len(quantity)):
    if quantity[i] > (len(binary) / 2):
        quantity[i] = 1
    else:
        quantity[i] = 0

stringNumbr = str(convert(quantity))
gamma = int(stringNumbr, 2)

for i in range(len(quantity)):
    if quantity[i] == 1:
        quantity[i] = 0
    else:
        quantity[i] = 1

stringNumbr = str(convert(quantity))
epsilon = int(stringNumbr, 2)

print("final result(epsilon*gamma): ", epsilon * gamma)
