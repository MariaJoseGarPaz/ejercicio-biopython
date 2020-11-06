from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os
import sys
filename= os.path.abspath("data/NC_002703.gbk")
seq1= "attAg"
seq2= "ggct"
def summarize_contents(filename):
        FileList = []
        File_Extension = []

        FileList = os.path.split(filename)
        File_Extension = os.path.splitext(filename)

        if(File_Extension[1] == ".gbk"):
                type_file= "genbank"
        else:
                type_file= "fasta"
                pass

        records = list(SeqIO.parse(filename, type_file))
        diccionario = {}

       
        diccionario['File: ']= FileList[1]
        diccionario['Path: ' ]= FileList[0]
        diccionario['num_records=' ]= len(records)

        diccionario['Name:'] = []
        diccionario['-ID:'] = []
        diccionario['Description: '] = []
        for seq_record in SeqIO.parse(filename, type_file):
                diccionario['-ID:'].append(seq_record.name)
                diccionario['Name:'].append(seq_record.id)
                diccionario['Description: '].append(seq_record.description)
        return diccionario
def concatenate_and_get_reverse_of_complement(sequence_a, sequence_b):

        SEQuence_a= Seq(sequence_a)
        SEQuence_b = Seq(sequence_b)
        concatenated= (SEQuence_a + SEQuence_b)
        reverse = concatenated.reverse_complement()
        return reverse.upper()

if __name__ == "__main__":
        resultado = summarize_contents(filename)
        print(resultado)
        ReverseComplement = concatenate_and_get_reverse_of_complement(seq1, seq2)
        print(ReverseComplement)
