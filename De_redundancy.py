import os
import sys



def main(DIR,OD):
    for file in os.listdir(DIR):
        if file.endswith(r'.fastq'):
            fastq=os.path.join(DIR,file)
            fasta=fastq.replace(r'.fastq','.fasta')
            output=os.path.join(OD,file.replace(r'.fastq',r'.fasta'))
            
            os.system(f'''
            seqtk seq -A {fastq} > {fasta}
            fastx_collapser -i {fasta} -o {output}
            rm {fasta}
            ''')
            print(f'''--->{file.replace(r'.fastq','')} *** DONE ''')
            
            


if __name__ == '__main__':
    for i in range(len(sys.argv)):
        if '-dir'==sys.argv[i]:
            DIR=sys.argv[i+1]
        elif '-OD'==sys.argv[i]:
            OD=sys.argv[i+1]
            os.system(f'''
            mkdir {OD}
            ''')
            main(DIR,OD)

# python De_redundancy.py -dir C_PopReads -OD D_DrResult