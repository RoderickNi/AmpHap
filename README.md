# AmpHap
AmpHap (Amplicons to Haplotypes) is a Python script designed for Linux-based operating systems, developed by various third-party programs including fastp, flash, seqtk, and fastx_toolkit. AmpHap takes as input the paired-end sequencing results in FASTQ format (RawReads_1.fastq, RawReads_2.fastq) and a file containing information of population-specific primers (primer.tab). AmpHap ultimately generates the haplotypes and their frequencies for targeted amplification regions of different populations in FASTA format.

## Usage
python MainScript.py     
--RawFq1 Reads1.fq \
                     --RawFq2 Reads2.fq \
                     --Primers Primer.tab \ # Primer and Samp_Size information    
                     --ReadType (string) \ # PE150 or PE250 (default: PE250)     
                     --SeqLen (int) \ # Mean Length of Amplicon      
                     --Bias (int) \ # Amplicon length variation permitted      
                     --Regulation (int) \ # Increase or decrease the filtering threshold based on 1/2N (N:Sample Size)      
                     --CPU (int)\ # Number of processors used      
                     
