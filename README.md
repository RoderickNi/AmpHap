# AmpHap
A python script for analysing NGS-based(illumine platform) amplicon sequencing result 

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
                     
