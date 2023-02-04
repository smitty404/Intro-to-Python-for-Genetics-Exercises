#Polypeptide analysis

#Given some polypeptide sequence, write code that
# a) assess wheter the polypeptide sequence has methionine (M) or not
# b) Asses wheter the polypeptide sequence has more than 10 aa's or not

polypeptide = 'ABHMMYFFEHBVA'


if len(polypeptide) > 10:
    if 'M' in polypeptide:
        print("This polypeptide has more than 10 aa's and contains methionine.")
    else:
        print("This polypeptide has more than 10 aa's and does not contain methionine.")
else:
    if 'M' in polypeptide:
        print("This polypeptide has less than 10 aa's and contains methionine.")
    else:
        print("This polypeptide has less than 10 aa's.")
