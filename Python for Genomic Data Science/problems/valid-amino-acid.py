# Problem.
# Find if all characters in a given protein sequence are valid amino acids.

# Pseudocode
# for each character in protein sequence :
# if character is not amino acid :
# print invalid character and its position in protein


protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print("protein contains invalid amino acid %s at position %d" %
              (protein[i], i))


# ==============================================================================================================

# Problem.

# Suppose we are only interested in Hinding if a protein sequence is valid,
# not where are all the invalid characters in the sequence

protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print('this is not a valid protein sequence!')
        break

# ==============================================================================================================

# Problem.
# Delete all invalid amino acid characters from a protein sequence.

protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
corrected_protein = ''
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        continue
    corrected_protein = corrected_protein+protein[i]
print("Corrected protein sequence is:%s" % corrected_protein)
