#!/usr/bin/env python3
"""
Script to count k-mers in a FASTA file
"""

def read_fasta(filename):
    """Read a FASTA file and return the sequence"""
    sequence = ""
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('>'):  # Skip header lines
                sequence += line
    return sequence

def count_kmers(sequence, k):
    """Count k-mers in a sequence"""
    kmers = {}
    total_kmers = 0
    
    # Generate all k-mers
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers[kmer] = kmers.get(kmer, 0) + 1
        total_kmers += 1
    
    return kmers, total_kmers

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python count_kmers.py <fasta_file> [k_value]")
        print("Default k value is 3")
        sys.exit(1)
    
    filename = sys.argv[1]
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    # Read sequence
    sequence = read_fasta(filename)
    print(f"Sequence length: {len(sequence)} bp")
    print(f"K-mer size (k): {k}")
    print("-" * 50)
    
    # Count k-mers
    kmers, total_kmers = count_kmers(sequence, k)
    
    print(f"Total number of k-mers: {total_kmers}")
    print(f"Number of unique k-mers: {len(kmers)}")
    print("-" * 50)
    
    # Show top 10 most frequent k-mers
    print("\nTop 10 most frequent k-mers:")
    sorted_kmers = sorted(kmers.items(), key=lambda x: x[1], reverse=True)
    for i, (kmer, count) in enumerate(sorted_kmers[:10], 1):
        print(f"{i}. {kmer}: {count} times")
    
    # Optional: Save all k-mers to a file
    save = input("\nSave all k-mer counts to a file? (y/n): ")
    if save.lower() == 'y':
        output_file = f"kmers_k{k}.txt"
        with open(output_file, 'w') as f:
            f.write(f"K-mer\tCount\n")
            for kmer, count in sorted_kmers:
                f.write(f"{kmer}\t{count}\n")
        print(f"K-mer counts saved to {output_file}")

if __name__ == "__main__":
    main()
