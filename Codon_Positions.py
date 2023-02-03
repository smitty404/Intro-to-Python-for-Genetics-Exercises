#Position of star and termination codons
#Write code that a)returns the postion where the start and termination codons begin
# b) extracts the ORF(open reading frame, or the exon) of the RNA sequence)

#start: AUG, termination: UGA, UAA, UAG


rna = 'AAAAUGUUUCCCGCGGCGGCGUGAUUUAGCGAC'

start = rna.find('AUG')
termination = rna.find('UGA')

orf = rna[start:termination+3]

print(orf)