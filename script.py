from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os
filename= "/mnt/c/Users/alma_/Desktop/ls_orchid.gbk"
def summarize_contents(filename):
	all_records=[]
	records = list(SeqIO.parse(filename, "genbank"))
	print ("Path: ", os.path.dirname(filename))
	print("num_records = %i records" % len(records))
	print("\n\n")
	counter=1
	for seq_record in SeqIO.parse(filename, "genbank"):
		all_records.append(seq_record.name)
		print(counter, ".-")
		print("Name: ", seq_record.name)
		print("ID:",seq_record.id)
		print("\n")
		print ("Location: ")
		for seq_feature in seq_record.features :
                        print('Start: %d, Stop: %d'%(int(seq_feature.location.start),int(seq_feature.location.end)))
		print("\n")
		counter=counter+1
		##Aqui debe ir lo de location
summarize_contents(filename)

