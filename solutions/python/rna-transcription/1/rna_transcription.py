def to_rna(dna_strand):
    dna_map = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    result = ''
    for element in dna_strand:
        result += dna_map[element]
    return result
    
    
