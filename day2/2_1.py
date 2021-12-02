f = open('data.txt', 'r')
content = f.readlines()
times_incremented = 0
previous_depth = None
moves = []
quantity = []
for line in content:
    moves.append(line.split()[0])
    quantity.append(int(line.split()[1]))

horizontal = 0
depth = 0
for i in range(len(moves)):
    if moves[i] == 'forward':
        horizontal += quantity[i]
    elif moves[i] == 'down':
        depth += quantity[i]
    else:
        depth -= quantity[i]

print('final result (depth*horizontal): ', depth*horizontal)

f.close()
