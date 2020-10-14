from Bio.Seq import Seq
from Bio import SeqIO
from Bio import SeqFeature
from Bio SeqRecord import record
def summarize_contents(filename):
        record=SeqIO.read ("filename","genbank")
        print(record)
