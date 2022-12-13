def getCodons():
    sequenceADN = input("entrer la séquence d'ADN : ")
    if len(sequenceADN) == 0: #séquence test si l'utilisateur ne remplit pas la séquence
        sequenceADN = "ATGCGGAGATTATCGAGCATATAA" 
    codons = []

    for i in range (0, len(sequenceADN), 3):

        newCodon = sequenceADN[i:i+3]
        codons.append(newCodon)
    print(codons)
    return codons


aas= (
    ("A", ["GCA", "GCC", "GCG", "GCT"], "Ala"),
    ("C", ["TGC", "TGT"], "Cys"),
    ("D", ["GAT", "GAC"], "Asp"),
    ("E", ["GAA", "GAG"], "Glu"),
    ("F", ["TTC", "TTT"], "Phe"),
    ("G", ["GGT", "GGC", "GGA", "GGG"], "Gly"),
    ("H", ["CAT", "CAC"], "His"),
    ("I", ["ATA", "ATC", "ATT"], "Ile"),
    ("K", ["AAA", "AAG"], "Lys"),
    ("L", ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"], "Leu"),
    ("M", ["ATG"], "Met"),
    ("N", ["AAC", "AAT"], "Asn"),
    ("P", ["CCT", "CCC", "CCA", "CCG"], "Pro"),
    ("Q", ["CAA", "CAG"], "Gln"),
    ("R", ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"], "Arg"),
    ("S", ["AGT", "AGC", "TCA", "TCC", "TCG", "TCT"], "Ser"),
    ("T", ["ACT", "ACC", "ACA", "ACG"], "Thr"),
    ("V", ["GTT", "GTC", "GTA", "GTG"], "Val"),
    ("W", ["TGG"], "Trp"),
    ("Y", ["TAT", "TAC"], "Tyr"),
    ("STOP", ["TAG", "TAA", "TGA"], "STOP")
)

#sequenceADN = "AGTCGGAGATTATCGAGCATA"

#print(getCodons(sequenceADN))

codons = getCodons()
nomAA = []

for codon in codons:
    for aa in aas:
        if codon in aa[1]:
            nomAA.append(aa[2])

print(nomAA)

proteines = []

proteine_en_cours = []


for nom in nomAA:
    if nom == "STOP":
        proteines.append(proteine_en_cours)
        proteine_en_cours = []

    else:
        proteine_en_cours.append(nom)

proteines.append(proteine_en_cours)

print(proteines)