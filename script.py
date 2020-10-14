from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
        record = SeqIO.read(filename, "genbank")
        print("Name: ", record.name)
        ##Aqui debe ir lo de la ruta (path)
        records = list(SeqIO.parse(filename, "genbank"))
        print("num_records = %i records" % len(records))

        for seq_record in SeqIO.parse(filename,"genbank"):
                print("ID:",record.id)
                ##Aqui debe ir lo de location
summarize_contents(filename)
