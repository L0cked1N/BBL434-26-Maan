import sys

def fasta_length(fasta_file):
    seq = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if not line.startswith('>'):  # skip header
                seq.append(line.strip())
    return len(''.join(seq))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fasta_length.py <input.fasta>")
        sys.exit(1)

    fasta_path = sys.argv[1]
    length = fasta_length(fasta_path)
    print(f"Sequence length: {length}")
