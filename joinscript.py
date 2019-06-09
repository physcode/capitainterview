#initialise both empty dictionaries and load data files
dataL = open("test_data_01.csv","r")
dataR = open("test_data_02.csv","r")
listL = []
listR = []
joinedlist = []

def csvtoarray(file,array,delim=","):
    """Takes a file delimited by some delim character (csv by default)
     and returns a list of lists(array) of the file"""
    line = ''
    for line in file:
        line = line.strip('\n')
        splitstring = line.split(delim)
        array.append(splitstring)

csvtoarray(dataL,listL)
csvtoarray(dataR,listR)

def LEFTJOIN(LEFT,RIGHT,L_ON,R_ON,RESULT):
    """Takes a left and right array and left joins them according to
    the zero indexed ON keys. Returns a RESULT array"""
    for L in LEFT:
        countmatch = 0
        for R in RIGHT:
            if L[L_ON] == R[R_ON]:
                countmatch = countmatch + 1
                RESULT.append(L+R)
        if countmatch == 0:
            RESULT.append(L+['NULL'])
    keys = LEFT[0] + RIGHT[0]
    RESULT[0] = keys

LEFTJOIN(listL,listR,1,0,joinedlist)
print("The left join produced a table with " +str(len(joinedlist)-1) +" rows!")

def concatlist(lst):
    """Concatenates all the lists in a string in preparation
    for loading into the final csv file"""
    result = ''
    for element in lst:
        result += ',' + str(element)
    result = result[1:]
    return result

dest = open('joined.csv','w')
for row in joinedlist:
    dest.write(str(concatlist(row))+'\n')
dest.close()


input("Success! The LEFT JOINED csv is found in joined.csv")
