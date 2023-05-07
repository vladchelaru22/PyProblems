def func(note, nume_materie):
    """
    Trebuie sa creati un tuplu cu numele "pereche",
    in care veti tine, astfel, (media notelor, numele_materiei)
    exemplu: pereche = (...)
    """

    ################### TO DO #########################
    media=0
    for i in note:
        media+=i

    media=media/len(note)
    pereche=(media,nume_materie)
    ###################################################

    return pereche
