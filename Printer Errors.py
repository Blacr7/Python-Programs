from collections import Counter
from fractions import Fraction

def printer_error(s):
    errorLetters = ('n','o','p','q','r','s','t','u','v','w','x','y','z')

    count = Counter(s)

    errorRate = sum(count[i] for i in errorLetters)

    return str(errorRate) + '/' + str(len(s))
    
printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')
