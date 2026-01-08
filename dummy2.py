
def count_fasta_records(filename):
    """Count the number of records in a FASTA file"""
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                count += 1
    return count

# Count records
num_records = count_fasta_records('seq.mfa')
print(f"Number of records: {num_records}")
