def func(size):

    romb = ""

    ################### TO DO #########################

    #verificăm dacă size este par sau impar. Dacă este par, îl incrementăm cu 1 pentru a menține simetria
    if size % 2 == 0:
        size += 1
    middle = size // 2 #linia din mijloc
    for i in range(size):
        if i <= middle:
            spaces = middle - i
            dots = i * 2 + 1
        else:
            spaces = i - middle
            dots = (size - i - 1) * 2 + 1
        romb += ' ' * spaces + '@' + '.' * (dots - 1) + '@' + '\n'

    return romb