import sys
import os

for i in range(len(sys.argv)):
    if '--RawFq1' == sys.argv[i]:
        fq1=sys.argv[i+1]
    elif '--RawFq2' == sys.argv[i]:
        fq2=sys.argv[i+1]
    elif '--Primers' == sys.argv[i]:
        primer_info = sys.argv[i+1]
    elif '--ReadType' == sys.argv[i]:
        RT = sys.argv[i+1]
    elif '--SeqLen' == sys.argv[i]:
        SL = sys.argv[i+1]
    elif '--Bias' == sys.argv[i]:
        BS = sys.argv[i+1]
    elif '--Regulation' == sys.argv[i]:
        REG = sys.argv[i+1]
    elif '--CPU' == sys.argv[i]:
        N = sys.argv[i+1]
    
print("======Step_1 QC======")
os.system(f'''
mkdir A_QC
fastp --in1 {fq1} --in2 {fq2} --out1 ./A_QC/clean_1.fq --out2 ./A_QC/clean_2.fq --qualified_quality_phred 20 --unqualified_percent_limit 0 --n_base_limit 1 --correction --thread {N}
mv fastp.html ./A_QC/fastp.html
mv fastp.json ./A_QC/fastp.json
mkdir ./A_QC/statistic
fastqc -t {N} -o ./A_QC/statistic ./A_QC/clean_1.fq ./A_QC/clean_2.fq
''')

print("======Step_2 Overlapping======")
os.system(f'''
python Overlapping.py -fq1 ./A_QC/clean_1.fq -fq2 ./A_QC/clean_2.fq -SequenceLength {SL}_{BS} -OD ./B_Overlapping -readtype {RT} -cpu {N}
''')

print("======Step_3 Separating======")
os.system(f'''
python Separator.py -fq ./B_Overlapping/out.extendedFrags.fastq -Pp {primer_info} -OD C_PopReads
''')

print("======Step_4 Same Reads Mergering and Counting======")
os.system(f'''
python De_redundancy.py -dir C_PopReads -OD D_DrResult
''')

print("======Step_5 Reads Filtering======")
os.system(f'''
python Filter_haplotype.py -dir D_DrResult -Pp {primer_info} -OD E_HapFilter -Reg {REG}
''')

print("======Step_6 Haplotypes Identification======")
os.system(f'''
python Haplotype_identification.py -dir E_HapFilter -OD F_Haplotypes
echo DONE
''')

print("======Step_7 Haplotypes in Populations======")
os.system(f'''
python Finaloutput_Haplotypes.py -hap F_Haplotypes -filter E_hapFilter -OD G_PopHaplotypes 
''')
