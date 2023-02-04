#Biomolecule classifier
#Write code that takes a molecule as input and classify it as DNA or RNA by using conditional statements

mol = str(input("Enter DNA or RNA molecule: ")).upper()

if 'T' in mol:
    print("This is a DNA molecule.")
elif 'U' in mol:
    print("This is a RNA molecule")