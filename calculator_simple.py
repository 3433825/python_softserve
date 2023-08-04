def calc(example):
    DIVIDING_BY_ZERO = ['/0']
    INVALID_SYMBOLS = [',','?','!',';',':','&','@','#','$','%','^','=']
    ERR_START_LINE = ['+','-','*','/']
    ERR_END_LINE = [')+',')-',')*',')/','+','-' ,'*','/']
    ERR_NUMBER_MISS = ['(+', '(-', '(*', '(/', '+)', '-)', '*)', '/)',
                       '++', '+-', '+*', '+/', '-+', '--', '-*', '-/',
                       '*+', '*-', '**', '*/', '/+', '/-', '/*', '//']

    ERR_MESS_DIVIDING_BY_ZERO = "Dividing by zero"
    ERR_MESS_SPACES_MISSED = "Spaces are missed"
    ERR_MESS_INVALID_SYMBOLS = "You entered invalid symbols"
    ERR_MESS_ALPHABET_SYMBOLS = "You entered alphabetic symbols"
    ERR_MESS_START_LINE = "Number is missing at the start of line"
    ERR_MESS_END_LINE = "Number is missing at the end of line"
    ERR_MESS_NUMBER_MISS = "Number is missing"

    all_symbols = example.split()
    STR_BEG = all_symbols[0]
    STR_END = all_symbols[-1]

    all_neighbours = []
    for i in list(range(len(all_symbols))):
        symbols_nearby = all_symbols[i - 1: i + 1]
        str = "".join(symbols_nearby)
        all_neighbours.append(str)

    if list(set(all_neighbours)&set(DIVIDING_BY_ZERO)):
        return ERR_MESS_DIVIDING_BY_ZERO
    elif [elem in elem for elem in all_symbols if len(elem) > 1 and not elem.isalnum()]:
        return ERR_MESS_SPACES_MISSED
    elif list(set(all_symbols)&set(INVALID_SYMBOLS)):
        return ERR_MESS_INVALID_SYMBOLS
    elif [symbol for symbol in all_symbols if symbol.isalpha()]:
        return ERR_MESS_ALPHABET_SYMBOLS
    elif [s for s in ERR_START_LINE if s == STR_BEG]:
        return ERR_MESS_START_LINE
    elif [w for w in ERR_END_LINE if w == STR_END]:
        return ERR_MESS_END_LINE
    elif list(set(all_neighbours)&set(ERR_NUMBER_MISS)):
        return ERR_MESS_NUMBER_MISS
    else:
        return eval(example)