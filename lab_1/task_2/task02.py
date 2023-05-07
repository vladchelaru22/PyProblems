def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """

    ################### TO DO #########################
    nume_formatat = ()
    num0 = []
    num1 = []
    num2 = []
    nume = ""
    for i in range(len(nume_complete)):
        space_pos = nume_complete[i].index(' ')
        line_pos = nume_complete[i].index('-')
        nume=nume_complete[i][:space_pos]
        num0.append(nume)
        nume=nume_complete[i][space_pos + 1:line_pos]
        num1.append(nume)
        if(i==len(nume_complete)-1):
            nume=nume_complete[i][line_pos + 1:-2]
            num2.append(nume)
        else:
            nume = nume_complete[i][line_pos + 1:]
            num2.append(nume)

    nume_formatat = (num0, num1, num2)

    return nume_formatat
