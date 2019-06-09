##Script written in Python3 - Nikolaos Palamidas##

def LEFTJOIN(Lfilename,Rfilename,LEFT_ON,RIGHT_ON,destination,delimiter = ","):
    """Takes arguments of a file name for the left and right tables
     (in working directory). Left joins according to the LEFT_ON and RIGHT_ON columns of each specified by zero indexed number.
    Delimiter is set to a comma as default"""
    dataL = open(Lfilename,"r")
    dataR = open(Rfilename,"r")
    listL = []
    listR = []
    joinedlist = []

    def csvtoarray(file,array,delim):
        """Takes a file delimited by some delim character (csv by default)
         and returns a list of lists(array) of the file"""
        line = ''
        for line in file:
            line = line.strip('\n')
            splitstring = line.split(delim)
            array.append(splitstring)

    csvtoarray(dataL,listL,delimiter)
    csvtoarray(dataR,listR,delimiter)

    def JOIN(LEFT,RIGHT,L_ON,R_ON,RESULT):
        """Takes a left and right array and left joins them according to
        the zero indexed ON keys. Returns a RESULT array"""
        for L in LEFT:
            countmatch = 0
            for R in RIGHT:
                if L[L_ON] == R[R_ON]:
                    countmatch = countmatch + 1
                    RESULT.append(L+R)
            if countmatch == 0:
                RESULT.append(L+['NULL','NULL'])
        keys = LEFT[0] + RIGHT[0]
        RESULT[0] = keys

    JOIN(listL,listR,LEFT_ON,RIGHT_ON,joinedlist)

    def concatlist(lst):
        """Concatenates all the lists in a string in preparation
        for loading into the final csv file"""
        result = ''
        for element in lst:
            result += delimiter + str(element)
        result = result[1:]
        return result

    dest = open(destination,'w')
    for row in joinedlist:
        dest.write(str(concatlist(row))+'\n')
    dest.close()
#END OF LEFTJOIN FUNCTION

#Left join the test files using the PD columns
LEFTJOIN("test_data_01.csv","test_data_02.csv",1,0,"joined.csv")
input("SUCCESS!!! joined.csv can now be found in the working directory...")
