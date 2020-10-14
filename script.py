from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import record
def summarize_contents(filename):
         
        record =SeqIO.read (filename,"genbank")
        print(len(record.features))
sumarize_contents(filename)
