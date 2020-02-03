import json
from workers import get_Offsets, get_InputEncoding
import sys
#Use to read the specs definition


specfile = 'C:\\Users\\adrian.oprea\\PycharmProjects\\RioTinto\\Latitude\\spec.json'
inFile = 'output.data'
outFile = 'output.csv'


def fixed_width2_csv(specfile,inFile,outFile):
    ## Get header offest
    output_format = ["%" + str(x) + "s," for x in get_Offsets(specfile)]
    ## strip the comma on the last element
    output_format[-1] = output_format[-1][:-1]
    ## move from input file to output file
    rf = open(inFile, 'r',encoding=get_InputEncoding(specfile))  # input file handle
    wf = open(outFile, 'w',)  # output file handle
    for row in rf.readlines():
        data_list = row.split()
        for offset in range(len(data_list)):
            wf.write(output_format[offset] % data_list[offset])
        wf.write("\n")
    rf.close()  # close input file handle
    wf.close()  # close output file handle

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    fixed_width2_csv(*sys.argv[1:])
