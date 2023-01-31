import os
import sys


'''

python Filter_haplotype.py -dir {} -Pp {} -OD {} -Reg {}

'''

def Threashold(primers,bias):
    load=open(primers,'r').read().split('\n')
    while '' in load:
        load.remove('')
    lst=[]
    for line in load:
        L=line.split('\t')
        N=int(L[3])
        T=1/(int((N*(1-float(bias))))*2) # 1/2N阈值
        lst.append([L[0],T])
    return lst

if __name__ == '__main__':

    for i in range(len(sys.argv)):
        if '-dir'==sys.argv[i]:
            DIR=sys.argv[i+1]
        elif '-Reg'==sys.argv[i]:
            bias = sys.argv[i+1]
        elif '-Pp'==sys.argv[i]:
            primers=sys.argv[i+1]
        elif '-OD'==sys.argv[i]:
            OTPT=sys.argv[i+1]
            os.system(f'''
            mkdir {OTPT}
            ''')
    primer_threashold_pop=Threashold(primers,bias)
    for element in primer_threashold_pop:
        for file in os.listdir(DIR):
            if file.endswith('.fasta') and file.replace(r'.fasta','') == element[0]:
                print('Filter reads in '+file+' with threashold (Frequency%) >= '+str(round(element[1]*100,5))+'%')
                fasta=open(os.path.join(DIR,file),'r').read().split('\n')
                while '' in fasta:
                    fasta.remove('')

                
                Total=0
                for i in range(len(fasta)):
                    if r'>' in fasta[i]:     
                        Total+=int(fasta[i].split('-')[1])   # 先计算每个种群的有效测序深度
                
                MinCount=Total*element[1]  # 再计算最小频数
                print(f'--->The count of Haplotype is greater than {round(MinCount,0)}')
                
                write_in = open(os.path.join(OTPT,file).replace('.fasta','_filter.fasta'),'a',encoding='utf-8')
                for i in range(len(fasta)):
                    if r'>' in fasta[i]:
                        T=int(fasta[i].split('-')[1])
                        if T >= MinCount:
                            print(fasta[i]+'\n'+fasta[i+1],file = write_in)
                write_in.close()

# python Filter_haplotype.py -dir D_DrResult -Pp primers.tab -OD E_HapFilter -Reg 0
