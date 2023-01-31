import os
import sys


'''
USAGE:

python Overlapping.py -fq1 <input: 1_fq> -fq2 <input: 2_fq> -SequenceLength <420_50> -OD <output: Result> -readtype <PE250 or PE150> -cpu

arg_lst:

-fq1
-fq2
-SequenceLength
-OD
-readtype
-cpu
'''


if __name__ in '__main__':

    # Overlapping
    cpu_num = 3
    readtype= 250
    for i in range(1,len(sys.argv)):
        if r'-fq1' in sys.argv[i]:
            fq1=sys.argv[i+1]
        elif r'-fq2' in sys.argv[i]:
            fq2=sys.argv[i+1]
        elif r'-OD' in sys.argv[i]:
            outputdir=sys.argv[i+1]
        elif r'-cpu' in sys.argv[i]:
            cpu_num=sys.argv[i+1]
        elif r'-readtype' in sys.argv[i]:
            if sys.argv[i+1] == 'PE250':
                readtype=250
            elif sys.argv[i+1] == 'PE150':
                readtype=150
        elif r'-SequenceLength' in sys.argv[i]:
            meanlength=sys.argv[i+1].split('_')[0]
            bias=sys.argv[i+1].split('_')[1]

    print('Overlapping with command')
    print(f'flash {fq1} {fq2} -d {outputdir} -t {cpu_num} -p 33 -r {readtype} -f {meanlength} -s {bias}')
            
    os.system(f'''
    
    flash {fq1} {fq2} -d {outputdir} -t {cpu_num} -p 33 -r {readtype} -f {meanlength} -s {bias}
    
    '''
    )

# python Overlapping.py -fq1 ./A_QC/clean_1.fq -fq2 ./A_QC/clean_2.fq -SequenceLength 400_100 -OD ./B_Overlapping -readtype PE250 -cpu 30
















        
