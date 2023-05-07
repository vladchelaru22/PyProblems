def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    def media(lst):
        return sum(lst) / len(lst)
    for x in register:
        if media(register[x])>=8.50:
            names.append(x)

     ###################################################
    
    return names
