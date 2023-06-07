def convert_elements(arg):
    for i in range(len(arg)):
        if type(arg[i]) == str:
            arg[i] = arg[i][0].upper() + arg[i][1:] + '?'
        elif type(arg[i]) == int:
            if arg[i] %2 == 0:
                arg[i] *= 2
            else:
                arg[i] += 1
        elif type(arg[i]) == bool:
            arg[i] = not arg[i]

    return arg

convert_elements(['test', 'c', 132, True])
