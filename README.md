# AmpHap description
AmpHap (Amplicons to Haplotypes) is a Python script designed for Linux-compatible operating systems, developed by various third-party programs including fastp, flash, seqtk, and fastx_toolkit. AmpHap takes as input the paired-end sequencing results in FASTQ format (RawReads_1.fastq, RawReads_2.fastq) and a file containing information of population-specific primers (primer.tab). AmpHap ultimately generates the haplotypes and their frequencies for targeted amplification regions of different populations in FASTA format.


## Dependencies
fastp v0.23.2 (https://github.com/OpenGene/fastp)    
FLASH v1.2.11 (https://github.com/dstreett/FLASH2)    
seqtk v1.3-r106 (https://github.com/lh3/seqtk)    
fastx_toolkit v0.0.14 (http://hannonlab.cshl.edu/fastx_toolkit/)    


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
                     

## Program execution flow
![image]([Program execution flow.tif](https://github.com/RoderickNi/AmpHap/blob/main/Program%20execution%20flow.tif)https://github.com/RoderickNi/AmpHap/blob/main/Program%20execution%20flow.tif)
