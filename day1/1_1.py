f = open('data.txt', 'r')  
content = f.readlines()
times_incremented = 0
previous_depth = None

for line in content:
    number = int(line)   #convert from string to int
    if previous_depth is None:
        previous_depth = number
    else:
        if number > previous_depth:
            times_incremented += 1
        previous_depth = number

print('times_incremented: ', times_incremented)
