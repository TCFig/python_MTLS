# Create a OOP project aroud DNA as a class and create different methods:
    # find restriction enzyme sites
    # find DNA motif 


class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def gc_content(self) -> float:
        """Calculate the GC content of a DNA sequence"""
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        gc_percentage = (c_count + g_count) / len(self.sequence)
        return gc_percentage

    def reverse_complement(self) -> str:
        """Get the reverse complement of a DNA sequence"""
        rc_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        rc_res = ''
        for c in self.sequence[::-1]:   # Reverse the sequence first
            rc_res += rc_dict[c]        # Direct lookup in the dictionary
        return rc_res
        # or this could be said only with 
        # > return ''.join([rc_dict[base] for base in self.sequence[::-1]])
    
    def complement(self) -> str:
        """Get the complement of a DNA sequence"""
        rc_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join([rc_dict[base] for base in self.sequence])
    
    def melting_temperature(self) -> float:
        """Calculate the melting temperature of DNA sequence"""
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        t_count = self.sequence.count('T')
        a_count = self.sequence.count('A')
        if len(self.sequence) < 14:
            return  (a_count+t_count) * 2 + (g_count+c_count) * 4
        return 64.9 +41*(g_count+c_count-16.4)/(a_count+t_count+g_count+c_count)

class RNASequence(DNASequence):
    def __init__(self, sequence):
        super().__init__(sequence.replace('T', 'U'))

    def reverse_complement(self) -> str:
        """Get the reverse complement of a DNA sequence"""
        rc_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        return ''.join([rc_dict[base] for base in self.sequence[::-1]])

    def divide_in_codons(self, seq: str=None) -> dict:
        """Divides the sequence in codons and obtain the 3 different reading frames of an RNA sequence"""
        # Use self.sequence if no specific sequence is provided
        seq = seq or self.sequence
        frames = {}
        for reading_frame in range(3):  # Loop through reading frames 0, 1, and 2
            frames[f'frame{reading_frame+1}'] = [seq[i:i+3] for i in range(reading_frame, len(seq) - 2, 3)]
        return frames

    def translate_RNA(self, min_protein_length:int=1) -> dict:
        """
        Trancribe an RNA sequence into a protein sequence. \
        The mmethod takes the 3 reading frames from the sequence and the reverse complement.\

        min_protein_length: the min length of the protein that should be returned. Use it to filter out small proteins.
        """
        proteins = {}

        def get_protein_seq(codon_list) -> list:
            """
            Function translates all the possible proteins from the RNA reading frames (that are between M and Stop codon),\
            and return the protein to a list if they are bigger than the min_protein_length
            """
            protein_list = []
            protein = ''
            codon_table = {
                "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
                "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
                "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
                "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
            }
            found_start = False
            start_positions = []  # List to keep track of methionine start positions

            for codon in codon_list:
                if codon == 'AUG':
                    found_start = True
                    start_positions.append(len(protein))  # Track start position of 'M'
                    protein += 'M'  # Add methionine to the protein sequence
                elif found_start:
                    if codon_table[codon] == 'Stop':
                        # Append the main protein and any subproteins starting from internal 'M'
                        for start_pos in start_positions:
                            subprotein = protein[start_pos:]
                            if len(subprotein) >= min_protein_length:
                                protein_list.append(subprotein)
                        
                        # Reset for the next protein
                        protein = ''
                        found_start = False
                        start_positions.clear()  # Clear the start positions as this protein is done
                    else:
                        protein += codon_table[codon]  # Add the amino acid to the protein
                            
            return protein_list if len(protein_list) > 0 else None
    
        possible_codons = self.divide_in_codons()
        possible_codons_rc = self.divide_in_codons(self.reverse_complement())

        for frame in possible_codons.keys():
            proteins[frame] = [get_protein_seq(possible_codons[frame])]
        for frame in possible_codons_rc.keys():
            proteins[f'{frame}_rc'] = [get_protein_seq(possible_codons_rc[frame])]

        return proteins
    
    def get_protein_seq_optimized(self, seq=None , min_protein_length=1) -> list:
        """
        Translates the RNA sequence between start codon (AUG) and stop codon in the same reading frame.
        Returns proteins only if their length is greater than or equal to the min_protein_length.

        This version is optimizied because it requires less time to work  due to the use of slicing
        rather than iterations.
        """
        seq = seq or self.sequence
        protein_list = []
        codon_table = {
            "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
            "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
            "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
            "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }

        start_pos = str(seq).find("AUG")  # Find the first start codon
        
        while start_pos != -1:  # Loop until no more start codons are found
            protein = "M"  # Start the protein with methionine (M)
            stop_pos = None
            
            # Search for the next stop codon within the same reading frame
            for i in range(start_pos + 3, len(seq) - 2, 3):
                codon = seq[i:i+3]
                if codon in ["UAA", "UAG", "UGA"]:  # Stop codon found
                    stop_pos = i
                    break
            
            if stop_pos:
                # Extract the codon sequence between start and stop codons
                coding_seq = seq[start_pos:stop_pos]
                
                # Translate the codon sequence into a protein sequence
                for j in range(3, len(coding_seq), 3):  # Skip the first codon (AUG), already added
                    codon = coding_seq[j:j + 3]
                    if codon in codon_table:
                        protein += codon_table[codon]
                        
                # Add the protein to the list if it meets the minimum length
                if len(protein) >= min_protein_length:
                    protein_list.append(protein)
                    
                # Now look for internal start codons within the same protein to extract subproteins
                for sub_start in range(1, len(protein)):
                    if protein[sub_start] == 'M':  # Found internal Methionine (M)
                        subprotein = protein[sub_start:]
                        if len(subprotein) >= min_protein_length:
                            protein_list.append(subprotein)

            # Look for the next start codon in the same frame
            start_pos = seq.find("AUG", stop_pos + 3 if stop_pos else start_pos + 3)
        
        return protein_list if protein_list else None



with open("./OOP_exercises/rosalind_orf.txt", 'r') as rnaseq:
    rna1 = RNASequence(rnaseq.readline().replace('\n', ''))

proteins_rna1 = rna1.translate_RNA(min_protein_length=1)
len(proteins_rna1.values())
print(proteins_rna1)
print(rna1.divide_in_codons())

rna2 = RNASequence('')
proteins_rna2 = rna2.translate_RNA(min_protein_length=1)
proteins_rna2_optimized = rna2.get_protein_seq_optimized()
rna2_rc = RNASequence(rna2.reverse_complement())
proteins_rna2_rc_optimized = rna2_rc.get_protein_seq_optimized()

#with open("./OOP_exercises/rosalind_orf_out.txt", 'w') as outfile:

for protein_list in proteins_rna1.values():
    print(protein_list)





