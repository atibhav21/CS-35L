#!/usr/bin/python
"""
	Copyright Atibhav Mittal 2016

"""

import sys
from optparse import OptionParser

def compareUnsorted(arr1, arr2, options):
    #arr1 = file1.getLines()
    #arr2 = file2.getLines()
    firstCol = ""
    secondCol = ""
    if(options.supress1 == False):
        firstCol = "\t"
    if(options.supress2 == False):
        secondCol = "\t"
    i = 0
    j = 0
    while(i < len(arr1) ):
        while(j < len(arr2)):
            if(arr2[j] == arr1[i] and options.supress3 == False):
                sys.stdout.write (firstCol + secondCol + str(arr1[i] ) ),
                i += 1
        		#delete element j from arr2
                del arr2[j]
                j = 0
                break
            else:
            	j += 1
        if(j >= len(arr2) and options.supress1 == False):  #unique to file 1
            sys.stdout.write(str(arr1[i])),
            i += 1
            j = 0
    j = 0
    if(options.supress2 == False):
        while(j < len(arr2)):
            sys.stdout.write (firstCol + (str(arr2[j]))),
            j += 1
      


#Prints out comm utility for sorted files
def compareFiles(arr1, arr2, options):  
    i = 0
    j = 0
    firstCol = ""
    secondCol = ""
    if(options.supress1 == False):
        firstCol = "\t"
    if(options.supress2 == False):
        secondCol = "\t"
    while i < len(arr1) and j < len(arr2): 
        if (arr1[i] == arr2[j]):
            if(options.supress3 == False):
                sys.stdout.write (firstCol + secondCol + str(arr1[i] ) ),
            i += 1
            j += 1
        elif (arr1[i] < arr2[j]):
            if(options.supress1 == False):
                sys.stdout.write (str(arr1[i])),
            i += 1
        elif (options.supress2 == False):
            sys.stdout.write (firstCol + (str(arr2[j]))),
            j+= 1
        else:
            j += 1
    if ( i < len (arr1) ):
        while i < len(arr1) :
            if(options.supress1 == False):
                sys.stdout.write (str(arr1[i])),
            i += 1
    elif (j < len (arr2) ):
        while j < len(arr2) :
            if(options.supress2 == False):
                sys.stdout.write (firstCol + str(arr2[j])),
            j += 1

def main():
    version_msg = "%prog 1.0"
    usage_msg = "usage: %prog [options] file1 file2"
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-u", "--unsorted", 
                     action="store_true", dest="m_unsorted",
                     help="Used for unsorted file input")
    parser.add_option("-1", action="store_true", default=False,dest="supress1")
    parser.add_option("-2", action="store_true", default=False, dest="supress2")
    parser.add_option("-3", action="store_true", default=False,dest="supress3")
    options, args = parser.parse_args(sys.argv[1:])
    try:    
        first_file = args[0]
        second_file = args[1]
        if(first_file == '-' and second_file == '-'):
            raise Exception
        if(first_file == '-'):
            for line in sys.stdin:
                arr1.append(line)
        else:
            f = open(first_file, 'r')
            arr1 = f.readlines()
            f.close()

        if(second_file == '-'):
            for line in sys.stdin:
                arr2.append(line)
        else:
            f = open(second_file, 'r')
            arr2 = f.readlines()
            f.close()

        if(options.m_unsorted):
            compareUnsorted(arr1, arr2, options)
        else:
            compareFiles(arr1, arr2, options)
    except:
	    sys.stdout.write("usage: comm [-123u] file1 file2"),
	    
if __name__ == "__main__":
    main()
