# Take the following function find_genes.py and...
# (done) 1. make gc-fraction an optional argument with default = 0.7 
# (done) 2. implement:
# --disabe_rc (done)
    # The assembly file only provides strands in one (arbitrary) direction. 
    # The user might want to find genes using also the GC-content on the reverse compliment strand. 
    # Add this as default behaviour,with the option to ignore reverse compliments.
# --verbose (done)
    # Add more diagnostic output to the user 
    # (e.g., which step or chromosome the program is currently working on)
# (done) 3. add try-except to your program to handle errors in parsing the fasta files. 
    # (malformatted fasta headers or strings that are not DNA or are empty)
    # it should print an error message about the fasta file being malformatted
# (done) 4. Edit the print function so that it actually saves something to output file

import argparse

def valid_dna_sequence(seq: str) -> bool:
    """Check if a string only has ATCG, meaning that it is a valid DNA string"""
    return set(seq).issubset({'A', 'T', 'C', 'G'})      # no need to put the small letters because with seq.upper they will alway be upper

def read_fasta(f) -> dict:
    seqs = {}
    for line in f:
        if line[0] == ">":
            acc = line.strip()
            seqs[acc] = ''
        else:
            seqs[acc] += line.strip().upper()           # make sure the dict it outputs always as upper case letters
    for string in seqs.values():
        if not valid_dna_sequence(string) or string == '':
            raise Exception(f'Error in fasta file: Invalid DNA string {string}.')
    return seqs

def reverse_complement(seqs) -> dict:
    rc = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
    rc_seqs = {}
    for chr, seq in seqs.items():
        out = ''
        for nc in seq:
            if nc in rc.keys():
                out += str(rc[nc])
        rc_seqs[chr+'_rc'] = out
    return rc_seqs

def get_kmer_windows(seq, w):
    return [seq[i:i+w] for i in range(len(seq) - w +1)]

def estimate_gc(kmers):
    return [(kmer.count('C') + kmer.count('G')) / len(kmer) for kmer in kmers]

def get_gene_regions(gc_fractions, gc_threshold):
    regions = []
    curr_region_start = 0
    for i in range(len(gc_fractions) - 1):
        # gene region starts
        if gc_fractions[i] < gc_threshold and gc_fractions[i+1] >= gc_threshold:
            curr_region_start = i+1
        # gene region is over
        elif gc_fractions[i] >= gc_threshold and gc_fractions[i+1] < gc_threshold:
            regions.append( (curr_region_start, i+1) )
    return regions

def print_results(chr_id, regions, outfile):
    """Write the results for each chromosome to the output file."""
    outfile.write(f"Chromosome: {chr_id}\n")
    outfile.write("Gene Regions:\n")
    for start, end in regions:
        outfile.write(f"Start: {start}, End: {end} \n")
    outfile.write("\n")

def main(args):

    try:
        seqs = read_fasta(args.assm_file)
        
    except FileNotFoundError:
        print(f'Error: The file {args.assm_file} does not exist in the current directory.')
        return
    except Exception as e:                          # Exception that identifies invalid DNA strings
        print(str(e))
        return
    except:
        print("There was an error related to parsing of fasta file. Please check the formatting of the file.")
        return

    if not args.disable_rc:
        seqs_rc = reverse_complement(seqs)
        seqs = {**seqs, **seqs_rc}

    for chr_id, seq in seqs.items():
        if args.verbose:
            print("Processing chromosome {0}".format(chr_id))
        kmers = get_kmer_windows(seq, args.w) # returns list of k-mers in order
        gc_fractions = estimate_gc(kmers) # estimates GC content per kmer, returns list of floats
        regions = get_gene_regions(gc_fractions, args.gc_threshold)
        print_results(chr_id, regions, args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find gene region \
                                     in a genome assembly through GC content.", \
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--w', type=int, default = 50, \
                        help='Window size to calculate GC content from')
    parser.add_argument('--gc_threshold', type=float, default = 0.7, \
                        help='threshold for GC content')
    parser.add_argument('assm_file', type=argparse.FileType('r'), \
                        help='input assembly file')
    parser.add_argument('outfile', type=argparse.FileType('w'),
                         help='Output .txt file')
    parser.add_argument('--disable_rc', action="store_true", \
                        help='Disable the use of reverse complements to find genes')
    parser.add_argument('--verbose', action="store_true", \
                        help='Print diagnostic output to terminal (stdout)')
    args = parser.parse_args()
    main(args) # Call the main function if run from terminal
