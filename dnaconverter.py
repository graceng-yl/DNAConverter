from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

inputname = input('Sequence file name (FASTA):')

rec = []
print('Sequences:')
for record in SeqIO.parse(inputname, "fasta"):
    print(record.id)

print('1. Reverse    2. Complement    3. Reverse Complement')
choice = input('Action:')

for record in SeqIO.parse(inputname, "fasta"):
    seq = record.seq
    if choice == '1':
        outseq = seq[::-1]
    elif choice == '2':
        outseq = seq.complement()
    elif choice == '3':
        outseq = seq.reverse_complement()
    rec.append(SeqRecord(outseq, id=record.id, description="", name=""))

outname = inputname.rpartition('.')[0]
SeqIO.write(rec, outname+'_converted.fasta', "fasta")
