Ordering of command lines used and output results:

The binding appears to occur at C and G heavy regions. I cant tell if other factors bind nearby, but going through
the motif output there are motifs in red, but some sequences have a smaller green or blue motif indicated
which may correspond to other factor binding sites? 

bowtie2-build chr19.fa chr19index.fa - get 6 output files

bowtie2 -x indexchr19.fa -q fastq-S output.sam

macs2 callpeak -t -c -g

sortnarrowpeaks.py

bedtools subtract [OPTIONS] -a <bed/gff/vcf> -b <bed/gff/vcf>

g1e is early so g-e is ctcf that turned off

e-g are ctcf that turned on

ctcf_sites_lost.bed
ctcf_sites_gained.bed

take e4 file- sort it in reverse order by column 5 (field4)
extract the sequence and make it like a fasta

sort -nrk5 er4peaks_peaks.narrowPeak | head -100 > er4_peaks_filtered_meme.bed

getfasta      Use intervals to extract sequences from a FASTA file.

/usr/local/opt/meme/bin/meme-chip er4_filtered_100.fa -meme-maxw 20 -o er4_motif.out

/usr/local/opt/meme/bin/meme-chip er4_filtered_100.fa -meme-maxw 20 -db JASPAR_CORE_2016.meme -o er4_motif_output.out 

meme out and meme.html 

file:///Users/cmdb/qbb2016-answers/lab-week5/er4_motif_output.out/meme_out/meme.html

er4_motif_output.out   push the whole directory probably. 

submit:
g1e_narrowpeaks_colomsorted
er4_narrowpeaks_colomsorted
ctcf_sites_gained.bed 
ctcf_sites_lost.bed 
er4_filtered_100.fa 
er4_peaks_filtered_meme.bed
motif_databases
motif logo.png
sortnarrowpeaks.py
