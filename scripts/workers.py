import json


def get_ColumnNames(specfile):
    with open(specfile, 'r') as myfile:
        data=myfile.read()
        myjson=json.loads(data)
        ColumnNames = []
        for cols in str(myjson['ColumnNames']).split(", "):
            ColumnNames.append(cols)
    return ColumnNames

def get_Offsets(specfile):
    with open(specfile, 'r') as myfile:
        data=myfile.read()
        myjson=json.loads(data)
        Offsets = []
        for offs in str(myjson['Offsets']).split(","):
            Offsets.append(offs)
    return Offsets

def get_OutputEncoding(specfile):
    with open(specfile, 'r') as myfile:
        data=myfile.read()
        myjson=json.loads(data)
        OutputEncoding = myjson['OutputEncoding']
    return str(OutputEncoding)

def get_InputEncoding(specfile):
    with open(specfile, 'r') as myfile:
        data=myfile.read()
        myjson=json.loads(data)
        InputEncoding = myjson['InputEncoding']
    return str(InputEncoding)

def get_IncludeHeader(specfile):
    with open(specfile, 'r') as myfile:
        data=myfile.read()
        myjson=json.loads(data)
        IncludeHeader = myjson['IncludeHeader']
    return IncludeHeader

def generate_header(specfile):
    header = ""
    empty = ' '
    for index, colname in enumerate(get_ColumnNames(specfile)):
            header+=colname + ((int(get_Offsets(specfile)[index])-1)*empty)
    return header

def generate_lines(specfile):
    s = ""
    for index, colname in enumerate(get_ColumnNames(specfile)):
        offset = get_Offsets(specfile)
        if colname == get_ColumnNames(specfile)[-1]:
            s+='t[0:' + get_Offsets(specfile)[index] + ']'
        else:
            s+='t[0:' + get_Offsets(specfile)[index] + '] + " "  + '
    s = '(' + s + ')'
    return str(s)
