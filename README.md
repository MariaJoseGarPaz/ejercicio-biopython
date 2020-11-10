# ejercicio-biopython
Archivo script.py:
Contiene 4 funciones:
	*Summarize contents:
	-Dado un archivo en formato .gbk o .fasta, lee los records del archivo y devuelve un diccionario con 
	el id, description y name de cada record
	-Así mismo, devuelve al usuario, la ruta, nombre del archivo y el resumen como se menciona anteriormente.
	

	*concatenate_and_get_reverse_of_complement(, ):
	-Dadas dos cadenas, estas son convertidas a objetos Seq, los cuales se concatenas y devuelve el reverso complementario
		de ambas cadenas

	*def print_protein_and_codons_using_standard_table(sequence):
	-Dada una secuencia de nucleótidos, se devuelve un diccionario con la secuencia transcrita (es decir, el mRNA, las proteínas (SOLO SI HAY START Y STOP CODON)
		y devuelve los stop codons de las proteínas
	-Usa la tabla estándar
	
	*def print_proteins_and_codons_using_mitocondrial_yeast_table(sequence):
	-Dada una secuencia de nucleótidos, se devuelve un diccionario con la secuencia transcrita (es decir, el mRNA, las proteínas (SOLO SI HAY START Y STOP CODON)
                y devuelve los stop codons de las proteínas
        -Usa la tabla de la mitocondria de la levadura. 
El archivo test_script:
	-Contiene una clase que a su vez tiene cuatro funciones:
		*test_summarize_contents()
		*test_concatenate_and_get_reverse_of_complement()
		*test_print_protein_and_codons_using_standard_table()
		*test_print_protein_and_codons_using_mitocondrial_yeast_table()
	-Las cuatro funciones tienen distintos casos de prueba para comprobar los resultados esperados.
