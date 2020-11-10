from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Data import CodonTable
import os
import sys
filename= os.path.abspath("data/NC_002703.gbk")
seq1= "attAg"
seq2= "ggct"
sequence =" "
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
def print_protein_and_codons_using_standard_table(sequence):


        #Conversión de string a Seq
        DNAsequence= Seq(sequence)
        
        diccionario={}

        #Definición de las keys del diccionario 
        diccionario['mRNA']= DNAsequence.transcribe().upper()
        diccionario['proteins'] = []
        diccionario['stop_codons'] = []
        
        #Traducción usando la tabla standard
        Amino_Acid = DNAsequence.translate(table= "Standard")
        i = 0

        #Ciclo que recorre la secuencia buscando codones de inicio y de paro para añadirlo a la lista proteins
        while i < (len(DNAsequence)):
                if (DNAsequence[i*3:i*3+3].upper() == "TTG") or (DNAsequence[i*3:i*3+3].upper() == "CTG") or (DNAsequence[i*3:i*3+3].upper() == "ATG"):
                        
                        if i+1 == len(DNAsequence):
                                diccionario['proteins'].append(Amino_Acid[i:])
                                break
                        j = i+1
                        while j < (len(DNAsequence)):
                                if(DNAsequence[j*3:j*3+3] == "TAG" ) or (DNAsequence[j*3:j*3+3] == "TAA") or (DNAsequence[j*3:j*3+3] == "TGA") :
                                        diccionario['proteins'].append(Amino_Acid[i:j])
                                        diccionario['stop_codons'].append(DNAsequence[j*3:j*3+3])
                                        i = j
                                        break
                                j= j+1
                #SI NO HAY CODON DE INICIO Y CODON DE PARO NO SE AGREGA A LA LISTA
                if((DNAsequence[i*3:i*3+3].upper() == "TTG") or (DNAsequence[i*3:i*3+3].upper() == "CTG") or (DNAsequence[i*3:i*3+3].upper() == "ATG")) and ((DNAsequence[j*3:j*3+3] == "TAG" ) or (DNAsequence[j*3:j*3+3] == "TAA") or (DNAsequence[j*3:j*3+3] == "TGA")):
                        diccionario['proteins'].append(Amino_Acid[i:j])
                        break
                i= i+1
                
                       
        
        
                        

        #Si la lista esta vacía, no hay codones de paro
        if diccionario['stop_codons'] == []:
                diccionario['stop_codons'] = "Not stop codons were found."   

        #Si la lista esta vacía, no hay proteínas
        if diccionario['proteins'] == []:
                diccionario['proteins'] = "Not proteins were found."
                
        
        return diccionario
                                

if __name__ == "__main__":
        proteins = print_protein_and_codons_using_standard_table(sequence)
        print(proteins)
