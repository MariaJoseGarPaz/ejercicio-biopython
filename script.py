from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os

def summarize_contents(filename):
        all_records=[]
        records = list(SeqIO.parse(filename, "genbank"))

        print ("Path: ", os.path.dirname(filename))
        print("num_records = %i records" % len(records))


        for seq_record in SeqIO.parse(filename, "genbank"):
                all_records.append(seq_record.name)
                print("Name: ", seq_record.name) 
                print("ID:",seq_record.id)
                        
                ##Aqui debe ir la position
                ##Aqui debe ir lo de location
summarize_contents(filename)
