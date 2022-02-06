result = ""

for i in range(9):
    for j in range(1,9):
        result += str(j+1) + ' * ' + str(i+1) + ' = ' + (str((j+1) * (i+1)) if (j+1) * (i+1) > 9 else ' ' + str((j+1) * (i+1))) + '\t'
    else:
        if i != 8:
            result += '\n'

print(result)
