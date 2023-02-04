base = str(input('Enter a nitrogen base: ')).upper()

while True:
    if base == 'A':
        print('This base is paired with T')
        break
    elif base == 'T':
        print('This base is paired with A')
        break
    elif base == 'C':
        print('This base is paired with G')
        break
    elif base == 'G':
        print('This base is paired with C')
        break
    else:
        print('Invalid base')
        break