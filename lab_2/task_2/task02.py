def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################
    for elem in args:
        if type(elem)==int:
            result.append(elem)
        if type(elem)==str and elem.islower() and len(elem) == 1:
            if elem not in ['a', 'e', 'i', 'o', 'u']:
                result.append(elem)
    ###################################################

    return result
