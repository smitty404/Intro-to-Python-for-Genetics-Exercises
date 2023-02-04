#Write python code that simulates the process of transcription from DNA to RNA

#seq = 'CCGTAGCGTAGC'

seq = str(input('Enter dna sequence: ')).upper()

rna = ''

for i in seq:
    if i == 'T':
        rna += 'U'
    else:
        rna += i

print(f'The RNA sequence is: {rna}')

