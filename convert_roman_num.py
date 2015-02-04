# -*- coding: utf-8 -*-

M = 1000
C = 100
X = 10
I = 1

def num_to_roman(number=2015):
    num_M  = number / M
    number = number % M
    num_C  = number / C
    number = number % C
    num_X  = number / X
    number = number % X
    num_I  = number

    # To String

    roman = 'M' * num_M

    if num_C == 9:
        roman += 'CM'
    elif num_C == 4:
        roman += 'CD'
    else:
        roman += 'D' * (num_C / 5)
        roman += 'C' * (num_C % 5)

    if num_X == 9:
        roman += 'XC'
    elif num_X == 4:
        roman += 'XL'
    else:
        roman += 'L' * (num_X / 5)
        roman += 'X' * (num_X % 5)

    if num_I == 9:
        roman += 'IX'
    elif num_I == 4:
        roman += 'IV'
    else:
        roman += 'V' * (num_I / 5)
        roman += 'I' * (num_I % 5)

    return roman

if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print num_to_roman(2015)
        print num_to_roman()
    else:
        print num_to_roman(int(argv[1]))
