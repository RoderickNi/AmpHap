import sys
import os





'''
python Haplotype_identification.py -dir {} -OD {}
'''






if __name__ == '__main__':
    
    for i in range(len(sys.argv)):
        if '-dir' == sys.argv[i]:
            DIR=sys.argv[i+1]
        elif '-OD' == sys.argv[i]:
            OTPT=sys.argv[i+1]
            os.system(f'''
            mkdir {OTPT}
            ''')
            
    Target_lst=[]        
    for file in os.listdir(DIR):
        if file.endswith('_filter.fasta'):
            #Pop=file.split('_')[0]
            Target=file.split('_')[1].split('-')[0]
            #Annotion=file.split('_')[1].split('-')[1]
            if Target not in Target_lst:
                Target_lst.append(Target)
    
            
    
    for target in Target_lst:
        SEQ_lst=[]
        for file in os.listdir(DIR):
            if file.endswith('_filter.fasta') and target in file:
                fasta=open(os.path.join(DIR,file),'r').read().split('\n')
                while '' in fasta:
                    fasta.remove('')
                for i in range(len(fasta)):
                    if r'>' in fasta[i]:
                        seq = fasta[i+1]
                        if seq not in SEQ_lst:
                            SEQ_lst.append(seq)
        write_in = open(os.path.join(OTPT,f'{target}_Haplotypes.fasta'),'a',encoding='utf-8')
        cnt=0
        for seq in SEQ_lst:
            cnt+=1
            name=f'>{target}_{str(cnt)}'
            print(name,file = write_in)
            print(seq,file = write_in)
        write_in.close()

# python Haplotype_identification.py -dir E_HapFilter -OD F_Haplotypes