result = ""
for i in range(1,9):
    for j in range(9):
        result += str(i+1) + ' * ' + str(j+1) + ' = ' + str((i+1) * (j+1)) + ' '
    else:
        if i != 8:
            result += '\n'
## MS
print(result)
