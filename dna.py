from csv import reader, DictReader
from sys import argv, exit

## python has csv module with reader and DictReader
##reader will read csv as list, DictReader will read file as dictionary
##python sys module gives access to sys.argv for command line arguments

## take two command line arguments
##first argument will be database, formatted as csv file, second will be dna sequence
def main():
    if len(argv) != 3:
        print("missing command line argument")
        exit(1)

    ##open the csv file
    ##open with open(filename)
    ##read its contents using f.read if f is the name of the file
    datacsv = open(argv[1], "r")
    database = list(reader(datacsv))
    #with open(argv[1], newline = '') as datacsv:
        #database = DictReader(datacsv) ##reads 1 row at a time
    numrows = 0
    for row in database:
        numrows = numrows + 1
    #print(numrows)
    #for row in database:
    numstrs = 0
    #for w in range(1, len(database[0]), 1): ##len database is number of rows (length of a column)
        #print(database[0][w])
        #numstrs = numstrs + 1
    #print(numstrs)
    #database = DictReader(open(argv[1])) ## I think this will read file into dictionary where key should be name (bc first value in row)
    ##database = open(argv[1], "r") ##not sure if argv is formatted properly, should open first provided command line argument

    with open(argv[2], newline = '') as seqcsv:
        sequence = seqcsv.read() ##reads entire thing into a string
        #print(sequence)
        ##seqlist = list(sequence)
    ##sequence = reader(open(argv[2]))

    ##get STR names from fieldnames
    ##creates a list of maxcount for each of the fieldnames starting at the second one, stored in list called "counts"
    numstr = 0
    counts = []
    for i in range(1, len(database[0]), 1):
        counts.append(STRcount(sequence, database[0][i]))
        numstr = numstr + 1
        #print(len(database[0][i]))
    #print(*counts)
    #print(numstr)
    #print(counts[0])

    ## for each row in the data, check if each STR count matches, if so, print out the person's name
    ## int(x) takes a string x and turns it into an integer
    ##to confirm a match, you'll need to check every column in the csv file other than the first one (which is name)

    for q in range(1, numrows, 1): ##for each row
        checksum = 0
        for z in range(1, len(database[0]), 1):  ##look in the column place to see if matches counts, length of first row
            if counts[z-1] == int(database[q][z]): ##second column compared to first count value
                checksum = checksum + 1
        if checksum == len(database[0]) -1:  ##if checksum matches number of STRs
            print(database[q][0]) ##then print the name (first value in row)
            datacsv.close()
            return ##end program
    print("No match") ##if not, print no match)
    datacsv.close()
    return

##compute individual STR counts
## i.e how many times do they repeat consecutively
##for each position in the sequence, compute how many times the STR repeats starting at that position
##i.e for each position, keep checking successive substrings until the STR repeats no longer
##i.e. check if matches once, then 2x, then 3x
## keep track of longest number of times
##len(s) gives you length of string s
## s[i:j] takes string s, returns the substring with all characters from the ith character up to (but not including) the jth

def STRcount (s, checkseq):
    precount = []
    for n in range(len(s)):
        freq = 0
        for i in range(n, len(s), len(checkseq)):
            j = i+len(checkseq)
            if s[i:j] == checkseq:
               freq = freq + 1
            else:
                break
        precount.append(freq)
    maxcount = 0
    for x in range(len(precount)):
        if precount[x] > maxcount:
            maxcount = precount[x]
    return maxcount

main()