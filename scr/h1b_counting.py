#import csv
import time
#from sys import argv


#Defining the CLASS for h1b_counting
class H1b_Counting():
    def __init__(self, input, chunk, n, keyName, output, ud, N2, caseStatus):
        self.input = input
        self.chunk = chunk
        self.n = n
        self.caseStatus = caseStatus
        self.keyName = keyName
        self.output = output
        self.ud = ud
        self.N2 = N2
#DsplitLine is a function that transforms the line with semicolon separated into
#a list of strings. I could have sliced the lines using the split function like
#split(";",n) to keep only the "n" elements on the right side if the line. Owing
#to the generality of the code, I've stored all the elements in the lines.

    def splitLine(self, l, delimiter =";"):
        line2 = l.split(delimiter)
        return line2

#splitQ is function that splits out the line with semicolon ignoring the ones within the double quotation marks
    
    def splitQ(self, line):
        next = line.split('\"')
        t0 =0
        t0 = time.time()
        tc0 =0
        tc0 = time.clock()
        i =0
        sd = []
        first = next[0].split(";")
        first.pop()
        sd = sd + first
        if (len(next) > 1):
            for s in next[1:len(next)]:
                if (s[0:1] != ";"):
                    #sd = sd + [s]
                    sd = sd + [""]
                    i += 1
                elif (i ==0):
                    sd =s.plit(";")
                else:
                    last = s.split(";")
                    last.pop(0)
                    sd =sd +last
        else:
            sd =next[0].split(";")
        t = time.time()
        tc = time.clock()
#print(i, t - t0, tc- tc0)
        return sd

    

#searchE is a function that searched through the list to find the index for a particular element
    def searchE(self,list,key):
        return list.index(key)

#cn is function to map the SOC code into SOC name.
#Note: it's more space effcicient to store integers (SOC code) rather than strings (SOC name).
#One can use a hash table (without collision) or dictionary to store the DATA
#I've used chunk method in this code rather than hash table so I've commented this function out

    '''
    def cn(code):
        cc = 0
        if (cc != code ):
            line = input.readline()
            next = splitLine(line)
            cc = next[SOCC]
        else:
            return next[SOCN]
    '''

#m_dict is function that creates a dictionary for both space and time optimization
#It looks through different item and adds the value of that particular item in the dictionary

    def m_dict(self, item, c ={}):
        self.c =c
        self.item = item
        if self.item in c.keys():
            c['{}'.format(self.item)] += 1
            return c
        else:
            c['{}'.format(self.item)] = 1
        return c

#top function writes the top n sorted (10 in the problem) parameters (meet the requirement
# like certified visa), number of occurance of that particular parameter and
# percentage (rounded), respectively seprated by semicolon
    def top(self, n, sd, nc, f):
        self.f = f
        self.n = n
        for i in range(n):
            perc = round((100*(sd[i][1] / float(nc))), 1)
            f.write("{};{};{}%\n".format(sd[i][0], sd[i][1], perc))

#merge is function to add (merge) two different dictionaries. It adds the value for the common
#keys and merges the rest
    def merge(self, d1, d2):
        result = d1
        for k in d2.keys():
            if k in d1.keys():
                result[k] = d1[k] + d2[k]
            else:
                result[k] = d2[k]
        return result

#dictF reads the input file line by line and stores the data into a chunck of dictionaries.
#For example in the case of occupation, the key in the dictionary is the occupation
#and number of the occurance of that particualr occupation is the value. At the end it
#uses the merge function to merge all the dictionaries step by step
#Note: the reason I used the chunk option is to utilize the multiprocessing libraries available in pythonself.
#The format of dictF function can be simply changed to write the dictionariies for each chunck
# We can run each chunck on different nodes and let it stores all the data at the endself.
# For this test, I wasn't sure if I was allowed to import multiprocessing libraries for python.
#Note: to speed dictF function first splits out the lines by only ;


    def dictF(self,N2, ud,  caseStatus='CERTIFIED'):
            ud ={}
            nC = 0
            nl =0
            self.c= {}
            self.caseStatus = caseStatus
            #N2 = int(nl / self.chunk)+1
            for i in range(self.chunk):
                for j in range(N2):
                    line = self.input.readline()
                    nl += 1
                    if line == '':
                        break
                    next = self.splitLine(line)
                    if next[CERT] == caseStatus:
                        next = self.splitQ(line)
                        nC += 1
                        ud = self.m_dict(next[self.searchE(header, keyName)], self.c)
                    if line == '':
                        break
            return ud, nC
            
#sortDict is sorting the elements of the dictionary alphabetically first
#and then based on its values.
    def sortDict(self, sd):
        return [v for v in sorted(sd.iteritems(), key=lambda(k, v): (-v,k))]





#Testing the class
if __name__ == "__main__":
    """
    argv corresonds to arguments passed on the command line.  Execute using
            argv[0]         arvg[1]
    python h1b_counting.py  input_file.txt
    """
    time_init = time.time()

    #input = argv[1]
    input = open("./input/h1b_input.csv", 'r')
    #noL is function which returns the number of lines in the file
    #to speed up the code it's better to remove it however one needs
    #to pick a large enough number for N2

    def noL(input):
        i = 0
        while True:
            line = input.readline()
            i += 1
            if line == '':
                break
        return i
    nl = noL(input)

    input.close()
    chunk = 10000
    N2 = int(nl /chunk)+1
    n =10
    input = open("./input/h1b_input.csv", 'r')
    caseStatus = "CERTIFIED"
    #writing the top "n" mostly occured occupations with  with certified visa
    keyName = 'SOC_NAME'
    top_10_occ = open("./output/top_10_occupations.txt",'w+')
    top_10_occ = open("./output/top_10_occupations.txt",'a')
    output = top_10_occ
    ud ={}
    PN = H1b_Counting(input, chunk, n, keyName, output, ud, N2, caseStatus)
    line = input.readline()
    header = PN.splitLine(line)
    SOCN = PN.searchE(header, 'SOC_NAME')
    SOCC = PN.searchE(header,  'SOC_CODE')
    CERT = PN.searchE(header, 'CASE_STATUS')
    ST = PN.searchE(header, 'EMPLOYER_STATE')
    output.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    #(sd, nC) = [PN.dictF(10, ud, caseStatus) for i in range(2)]
    #PN.dictF(10, ud, caseStatus)
    (sd, nC) = PN.dictF(N2, ud, caseStatus)
    sd = PN.sortDict(sd)
    PN.top(n,sd, nC, PN.output)
    PN.output.close()
    input.close()
    output.close()
    #writing the top "n" mostly occured occupations with certified visa
    input = open("./input/h1b_input.csv", 'r')
    top_10_st = open("./output/top_10_states.txt",'w+')
    top_10_st = open("./output/top_10_states.txt",'a')
    output = top_10_st
    ud ={}
    sd ={}
    keyName= 'EMPLOYER_STATE'
    PS = H1b_Counting(input, chunk, n, keyName, output, ud, N2, caseStatus)
    output.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    (sd, nC) = PS.dictF(N2, ud, caseStatus)
    sd = PS.sortDict(sd)
    PS.top(n,sd, nC, PS.output)
    output.close()
    #input_lines = input_file.readlines()
    input.close()

