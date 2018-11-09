#README
=====================================================================

#The Code is written in python 3
#I didn't import any external libraries (other than I/O). However, if I was allowed to import multiprocessing library,
#the code would have been more efficient to run each chunk on different nodes as it is explained in the code

#I have noticed there are several double quotation marks within the cvs file so I have two write a more advanced split function (called splitQ in my code) to ignore the semicolon with the quotation marks. 

#In order to store less data, I've transformed the data into the dictionary

#The code reads the code line by line and it stores the data into different dictionaries corresponding to different chunks.

#Here are the description of each individual function in the code:

#splitLine is a function that transforms the line with semicolon separated into a list of strings. I could have sliced the lines using the split function like split(";",n) to keep only the "n" elements on the right side if the line. Owing to the generality of the code, I've stored all the elements in the lines.

#I have noticed there are several double quotation marks within the cvs file so I have two write a more advanced split function (called splitQ in my code) to ignore the semicolon with the quotation marks. 

#searchE is a function that searched through the list to find the index for a particular element

************************************************************************************************************************************************************************************************************************************************
#optional:
#cn is function to map the SOC code into SOC name.

#Note: it's more space efficient to store integers (SOC code) rather than strings (SOC name).

#One can use a hash table (without collision) or dictionary to store the DATA
#I've used chunk method in this code rather than hash table so I've commented this function out
************************************************************************************************************************************************************************************************************************************************

#m_dict is function that creates a dictionary for both space and time optimization
#It looks through different item and adds the value of that particular item in the dictionary

#top function writes the top n sorted (10 in the problem) parameters (meet the requirement
#like the certified visa), number of occurrence of that particular parameter and
#percentage (rounded), respectively separated by a semicolon

#merge is a function to add (merge) two different dictionaries. It adds the value for the common
#keys and merges the rest

#dictF reads the input file line by line and stores the data into a chunk of dictionaries.
#For example in the case of occupation, the key in the dictionary is the occupation
#and the number of the occurrence of that particular occupation is the value. In the end,
#it uses the merge function to merge all the dictionaries step by step

#*Note: the reason I used the chunk option is to utilize the multiprocessing libraries available for python.

#The format of dictF function can be simply changed to write the dictionaries for each chunk

#We can run each chunk on different nodes and let it stores all the data at the end.

#For this test, I wasn't sure if I was allowed to import multiprocessing libraries for python.
#sortDict is sorting the elements of the dictionary alphabetically first
#and then based on its values.

#Testing the class: if __name__ == "__main__":

#For this code the chunk size = 100

#n is the number of rows in each output other than the header file. 

#For example for this problem, I was asked #to print 10 top occupations so, in this case, n= 10

#caseStatus is the different visa status. For example, in the problem, it is "CERTIFIED"

#keyName is the string name for the element we would like to be sorted. For example, for 10 occupations it is 'SOC_NAME'

#*Note: It is faster to store SOC codes in the dictionary and output. It is also more space efficient. One needs to simply map SOC_CODES into SOC_NAMES at the end. 




