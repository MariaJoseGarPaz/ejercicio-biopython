from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Data import CodonTable
import os
import sys
filename= os.path.abspath("data/NC_002703.gbk")
seq1= "attAg"
seq2= "ggct"
sequence ="ATGGCCATTGTAATGGGCCGCAAGGGTGCCCGATGAATGCCCATGTAATAATAA"
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
def print_proteins_and_codons_using_standard_table(sequence):
        DNAsequence= Seq(sequence)
        diccionario={}
        
        diccionario['mRNA']= DNAsequence.transcribe().upper()
        diccionario['proteins'] = []
        diccionario['stop_codons'] = []
        
        for i in range(0,len(DNAsequence)):
                if(DNAsequence[i*3:i*3+3] == "TAG" and i%3==0) or (DNAsequence[i:i+3] == "TAA" and i%3==0) or (DNAsequence[i:i+3] == "TGA" and i%3==0) :
                       
                        Amino_Acid = DNAsequence.translate()
                        print(DNAsequence.translate())


                        Proteins = Amino_Acid.split('*')
                                
                                
                        for i in range(len(Proteins)):
                                inicio = Proteins[i].find("M")
                                if inicio != -1:
                                        diccionario['proteins'].append(Proteins[i][inicio:])
                                if(diccionario['proteins']) == []:
                                        print ("Not found") 
                                        break
                        else:
                                break
        
                        
                        
        for i in range(len(DNAsequence)):
                if(DNAsequence[i*3:i*3+3] == "TAG" and i%3==0) or (DNAsequence[i*3:i*3+3] == "TAA" and i%3==0) or (DNAsequence[i*3:i*3+3] == "TGA" and i%3==0) :
                        if i-1 == len(DNAsequence):
                                break
                        else:
                                diccionario['stop_codons'].append(DNAsequence[i*3:i*3+3])
                        
                      
                
                     
                                
                
                
        if diccionario['stop_codons'] == []:
                diccionario['stop_codons'] = "Not found stop codons"   
                        
        print(diccionario)
                                

if __name__ == "__main__":
        resultado = summarize_contents(filename)
        print(resultado)
        ReverseComplement = concatenate_and_get_reverse_of_complement(seq1, seq2)
        print(ReverseComplement)
        proteins = print_proteins_and_codons_using_standard_table(sequence)
        print(proteins)
