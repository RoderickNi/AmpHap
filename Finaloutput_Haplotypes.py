import os
import sys

class Fasta:
    def __init__(self,fa_path):
        self.path = fa_path
        self.init_lst = [x for x in open(fa_path,'r').read().split('\n') if x != '']
        self.count = int(len([x for x in open(fa_path,'r').read().split('\n') if x != ''])/2)
    def Name_lst(self):
        lst=[]
        for i in range(0,self.count*2,2):
            lst.append(self.init_lst[i])
        return lst
    def Seq_lst(self):
        lst=[]
        for i in range(1,self.count*2,2):
            lst.append(self.init_lst[i])
        return lst
    def NameSeq_lst(self):
        lst=[]
        for i in range(0,self.count*2,2):
            lst.append((self.init_lst[i],self.init_lst[i+1]))
        return lst
        

def Hap2Pop(DirHap,DirPopFilter,OD):
    
    os.system(f'''
    mkdir {OD}
    ''')
    
    gene_dic={}
    for fileHap in os.listdir(DirHap):
        if fileHap.endswith(r'.fasta'):
            gene=fileHap.replace(r'_Haplotypes.fasta','')
            gene_NameSeq_lst=Fasta(os.path.join(DirHap,fileHap)).NameSeq_lst()
            gene_dic[gene]=gene_NameSeq_lst
            
            
            
    for gene,gene_NameSeq_lst in gene_dic.items():
        print(f'Doing {gene}')
        for fileFilter in os.listdir(DirPopFilter):
            if gene in fileFilter:
                write_in=open(os.path.join(OD,fileFilter.split('-')[0]+'_Haps.fasta'),'a',encoding='utf-8')
                for name,seq in Fasta(os.path.join(DirPopFilter,fileFilter)).NameSeq_lst():
                    for NAME,SEQ in gene_NameSeq_lst:
                        if SEQ==seq:
                            OTname=NAME+'\t'+'Frequency: '+name.split('-')[1]
                            print(OTname+'\n'+SEQ,file=write_in)
                write_in.close()
                print(f'''--->{fileFilter.split('-')[0]} *** DONE''')
                

if __name__ == '__main__':
    for i in range(len(sys.argv)):
        if '-hap' == sys.argv[i]:
            DirHap=sys.argv[i+1]
        elif '-filter' == sys.argv[i]:
            DirPopFilter=sys.argv[i+1]
        elif '-OD' == sys.argv[i]:
            OD=sys.argv[i+1]
    
    Hap2Pop(DirHap,
            DirPopFilter,
            OD)
            
            
            
 # python Finaloutput_Haplotypes.py -hap F_Haplotypes -filter E_hapFilter -OD G_PopHaplotypes           