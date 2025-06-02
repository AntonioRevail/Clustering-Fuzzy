# Clustering-Fuzzy

Fuzzy c-means
1 - The 10 sequences were aligned using MAUVE. Chromosomes 10, 28, and 31 were aligned separately.
 Website: https://darlinglab.org/mauve/mauve.html
 
2 - Join chromosomes 10, 28, and 31 of each species into separate .fasta files.

3 - Generate 5 additional sequences from one, using the code below.
 Code: modeljukescantor.py
 
4 - Combine all sequences from all species into a single .fasta file.
 Code: joinchromosomes.py
 
5 - Vectorize the sequences (convert the bases into numbers). Save the result into a .csv file.
 Code: vectorization.py
 
6 - Use the output file from step 5 (.csv) as input for Fuzzy c-means.
 Code: fcm.py
Note: The output of this code contains, separately, the membership degrees and the fuzzy partition coefficients. A better visualization would be to place this data in a spreadsheet to better observe the clusters.
 File: all_the_k.xlsx

Fuzzy Map
1 - This code builds a color plot showing the distribution of species across clusters.
 Code: fuzzy_ graphics_10.py
	fuzzy_ graphics_10.py

