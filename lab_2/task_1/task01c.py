def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################
    def pal(string):
        if string==string[::-1]:
                return True
        else:
            return False
    palindromes=filter(pal,words)

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
