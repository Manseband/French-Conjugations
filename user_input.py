def vrb():
    verb = input('Which verb would you like to conjugate: ').lower()

    if verb == '':
        verb = 'parler'

    return verb

def tns():
    tense = input('Which tense: ').lower()

    if tense == '':
        tense = 'present'

    return tense
