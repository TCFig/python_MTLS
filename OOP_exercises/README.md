# DNA & RNA Sequence Analysis Project

This project applies Object-Oriented Programming (OOP) principles to bioinformatics, specifically for DNA and RNA sequence analysis. Inspired by bioinformatics challenges on [Rosalind](https://rosalind.info/problems/list-view/), it uses Python to create reusable classes and methods that analyze nucleotide sequences, implement DNA-to-protein translations, and calculate properties relevant to molecular biology.

The project introduces `DNASequence` and `RNASequence` classes, each providing methods to solve key biological questions, such as identifying DNA motifs, GC content, and performing RNA translation into proteins. This structure provides a modular and extensible foundation for tackling more complex bioinformatics tasks.

## Classes and Methods
1. `DNASequence` Class
The `DNASequence` class models a DNA sequence and includes methods to analyze and interpret genetic data:

- `gc_content()`: Calculates the GC content, a critical factor in determining DNA stability.
- `reverse_complement()`: Provides the reverse complement sequence, essential for working with double-stranded DNA.
- `complement()`: Generates the complement of the DNA strand.
- `melting_temperature()`: Calculates the melting temperature, relevant for PCR optimization and assessing DNA binding stability.

2. `RNASequence` Class
Inherits from `DNASequence` but is specifically designed for RNA sequences, making necessary adjustments such as replacing T with U.

- `reverse_complement()`: Returns the reverse complement, modified to account for RNA's U base.
- `divide_in_codons()`: Divides the RNA sequence into codons across all reading frames.
- `translate_RNA()`: Translates the RNA sequence into potential proteins, accounting for start and stop codons. This method generates protein sequences from both forward and reverse reading frames, with an option to filter by minimum protein length.
- `get_protein_seq_optimized()`: An optimized method for translating RNA, leveraging slicing for better performance. It identifies proteins based on start (AUG) and stop codons, filtering for specified minimum protein lengths. **(under development)**

## Future Directions
This project can be extended with additional bioinformatics functionalities, including motif searches, restriction enzyme sites analysis, and variant calling methods, making it a versatile toolkit for sequence analysis tasks.

