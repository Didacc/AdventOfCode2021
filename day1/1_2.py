f = open('data.txt', 'r')
content = f.readlines()
times_incremented = 0
previous_depth = None
numbers = []
for line in content:
    number = int(line)
    numbers.append(number)

a = 0
i = 0
while i < (len(numbers)-2):
    for j in range(3):
        a += numbers[i + j]
    if previous_depth is not None:
        if a > previous_depth:
            times_incremented += 1
        previous_depth = a
    else:
        previous_depth = a
    a = 0
    i += 1
print('times_incremented: ', times_incremented)
