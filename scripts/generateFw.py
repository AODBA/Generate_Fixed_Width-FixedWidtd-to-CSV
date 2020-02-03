import random
from workers import generate_header, generate_lines, get_IncludeHeader, get_InputEncoding, get_ColumnNames
import sys
# Home namy rows
ROWS = 1000
# Just some sample data
SAMPLE = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
# Output Filename
output_filename = 'output.data'
# Specs Location
specfile = 'spec.json'


def generate(specfile, output_filename):
    if  get_IncludeHeader(specfile) == 'True':
        with open(output_filename, 'w',encoding=get_InputEncoding(specfile)) as outfile:
            for h in get_ColumnNames(specfile):
                outfile.write(generate_header(specfile) + '\n')
                for r in range(ROWS):
                    t = ''.join(random.sample(SAMPLE,len(SAMPLE)))
                    outfile.write(eval(generate_lines(specfile)) + '\n')
                outfile.close()
                return output_filename + ' was created, with '+  str(ROWS) + ' rows'
    else:
        with open(output_filename, 'w',encoding=get_InputEncoding(specfile)) as outfile:
            for r in range(ROWS):
                t = ''.join(random.sample(SAMPLE,len(SAMPLE)))
                outfile.write(eval(generate_lines(specfile)) + '\n')
            outfile.close()
            return output_filename + ' was created, with '+  str(ROWS) + ' rows'

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    generate(*sys.argv[1:])
