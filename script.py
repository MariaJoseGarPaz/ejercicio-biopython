from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import sys
filename= "/mnt/c/Users/alma_/Desktop/ejercicio-biopython/data/ls_orchid.gbk"
def summarize_contents(filename):
        FileList = []
        FileList = os.path.split(filename)
        cadena = " "
        cadena=("File: " + FileList[1])
        records = list(SeqIO.parse(filename, "genbank"))
        path=  os.path.dirname(filename)
        cadena+= ("\nPath: " + path)
        cadena+= ("\nnum_records= "+ str(len(records)))
        print("\n\n")
        for seq_record in SeqIO.parse(filename, "genbank"):
                cadena+= ("\n-ID: " + str(seq_record.id))
                cadena+=("\nName: " + str(seq_record.name))
                cadena+=("\nDescription: " + str(seq_record.description))
                cadena+= ("\n")
        return cadena
result=summarize_contents(filename)
print(result)
