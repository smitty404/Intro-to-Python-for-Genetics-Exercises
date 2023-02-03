#Calculating allele frequencies
#Write code that asks user the # of individuals w/ the genotypes pp, pq, and qq in the pop
#then return the frequencies of the two alleles in the population

pp = int(input("Number of people with genotype pp: "))
pq = int(input("Number of people with genotype pq: "))
qq = int(input("Number of people with genotype qq: "))

n_total = pp + pq + qq

freq_p = (2 * pp + pq) / (2*n_total)

freq_q = (2 * qq + pq) / (2*n_total)

print("The p allele frequency: ",round(freq_p,2),"%")

print("The q allele frequency: ",round(freq_q,2),"%")

