#Estimating recombination frequency
#Write a program that estimates gene distances based on the frequences of the recombinant
#genotypes and the non-recombinant genotypes (for two loci)

rec1 = int(input('Number of recombinant genotypes 1: '))
rec2 = int(input('Number of recombinant genotypes 2: '))

nonrec1 = int(input('Number of non-recombinant genotypes 1: '))
nonrec2 = int(input('Number of non-recombinant genotypes 2: '))

#recombination frequency

RF = (rec1+rec2)/(rec1+rec2+nonrec1+nonrec2) * 100

print("The recombination frequency is estimated to be", round(RF, 2), "%")
