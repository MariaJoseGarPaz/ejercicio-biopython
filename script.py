from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import sys
filename= "/mnt/c/Users/alma_/Desktop/bioinfo/ls_orchid.gbk"
def summarize_contents(filename):
        AllRecords=[]
        FileList = []
        FileList = os.path.split(filename)
        print("File : ", FileList[1])
        records = list(SeqIO.parse(filename, "genbank"))
        path=  os.path.dirname(filename)
        print ("Path: ", path)
        print("num_records = %i records" % len(records))
        print("\n\n")
        counter=1
        print("Records")
        for seq_record in SeqIO.parse(filename, "genbank"):
                AllRecords.append(seq_record.name)
                print(counter, ".-")
                print("-ID: ", seq_record.id)
                print("-Name: ", seq_record.name)
                print("-Description: ", seq_record.description)
                counter=counter+1
                print("\n")
summarize_contents(filename)
