# ejercicio-biopython
Archivo script.py:
Contiene 6  funciones:
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

	extract_sequences(file_name, formato):
	*Que dado un archivo que se espera que esta en formato fasta, devuelve N cantidad de archivos dependiendo del num_records en formato genbank
	
	extract_sequences_revcomp(file_name):
	-Que dado un archivo que se espera esta en formato fasta, devuelve otro archivo en formato fasta con las secuencias con el reverso
	complementario 
El archivo test_script:
	-Contiene una clase que a su vez tiene cuatro funciones:
		*test_summarize_contents()
		*test_concatenate_and_get_reverse_of_complement()
		*test_print_protein_and_codons_using_standard_table()
		*test_print_protein_and_codons_using_mitocondrial_yeast_table()
		*test_extract_sequences (Compara el num_records con el número de archivos generados y compara el contenido de cada archivo con el record correspondiente)
		*test_extract_sequences_revcomp( Compara el num_records del primer archivo con el del archivo generado
		y compara cada record con su reverso complementario)
	-Las cuatro funciones tienen distintos casos de prueba para comprobar los resultados esperados.
