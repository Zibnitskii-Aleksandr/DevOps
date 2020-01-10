import string
from functools import reduce
from random import randint

#____________________________________________________ Task 1
print("[ Task 1 ]", "-" * 50, "\n")
elm1 = int(input("First element Fibonacci sequence [ input ]: "))
elm2 = int(input("Second element Fibonacci sequence [ input ]: "))
lenseq = int(input("Fibonacci sequence length [ input ]: "))

# Init Fibonacci sequence
# .......................
def fibInit(a, b, num): 
    fibArray = [a, b]
    for i in range(2,num):
        elmn = int(fibArray[i-1]+fibArray[i-2])
        fibArray.append(elmn)
    return fibArray   

# Fibonacci sequence sum
# .......................
def fibSum(arr):
    return reduce(lambda x, y: x + y, arr)

myList = fibInit(elm1, elm2, lenseq)
print("." * 61)
print("Fibonacci sequence - ", myList)
print("Fibonacci sequence sum:", fibSum(myList), "\n")
#
#____________________________________________________ Task 2
print("[ Task 2 ]", "-" * 50, "\n")
len_list = int(input("Length list [input]: "))
srcFile = 'src_num.txt'
dstFile = 'dst_num.txt'

#def openFile(filename, openmode, datastring):
#    with open(filename, openmode) as myFile:
#        filename.write(datastring)
#    return filename    

# Create new file with randomize filling integer
# ..............................................
def makeNumFile(len_list):
    myString = ""
    int_arr = [randint(1, 16) for i in range(len_list)]
    myString = ",".join(map(str, int_arr))
    with open(srcFile, 'w') as myFile:
        myFile.write(myString)
    return myFile    

# Reading source file and delete even values
# Write result to destination file
# ..........................................
def changeNumFile(srcFile):
    srcList = dstList = []
    with open(srcFile, 'r') as myFile:
        tempdata = myFile.read()
        myFile.close()
        srcList = tempdata.split(",")
        dstList = list(filter(lambda x: (int(x)%2 != 0), srcList))
    with open(dstFile, 'w') as myFile:
        myFile.write(",".join(map(str, dstList)))
    return dstFile

print("." * 61)
makeNumFile(len_list)
changeNumFile(srcFile)

# Output work result
# ..................
print("Source file")
print(open(srcFile, 'r').read(),"\n")
print("Destination file")
print(open(dstFile, 'r').read(),"\n")
#
#____________________________________________________ Task 3
print("[ Task 3 ]", "-" * 50, "\n")

srcFile ='source_03.txt'
dstFile ='revers_03.txt'

srcData = dstData = []
srcText = dstText = ''
with open(srcFile) as myFile:
    srcData = myFile.read().splitlines()
    myFile.close()
    for i in range(len(srcData)):
        srcText = srcData[i].split()
        dstText = ' '.join(map(str, srcText[::-1]))
        dstData.append(dstText.strip())            
with open(dstFile, 'w+') as myFile:
    for i in range(len(dstData)):
        dstText = dstData[i]+'\n'
        myFile.write(dstText)
    myFile.close()

print("Source file","."*49)
print(open(srcFile, 'r').read(), "\n")
print("Destination file","."*49)
print(open(dstFile, 'r').read())
#
#____________________________________________________ Task 4
print("[ Task 4 ]", "-" * 50, "\n")

srcFile ='source_03.txt'
filtrCond = ('a','at','by','for','in','the','on','of')
dataExclude = []

def filtrWord(myString):
    flag = 0
    tempString = myString.lower()
    if (tempString in filtrCond):
        flag = 1
        dataExclude.append(myString)
    return flag

countTotal = countWord = 0
with open(srcFile) as myFile:
    srcData = myFile.read().split()
    countTotal = len(srcData)
    myFile.close()
for i in range(len(srcData)):
    if filtrWord(srcData[i]) != 1:
        countWord += 1
print("Source file","."*49)
print(open(srcFile, 'r').read(), "\n")
print("." * 61)
print("The total number of tokens: ", countTotal,"\n")
print("Total word count: ", countWord,"\n")
print("Excluded tockens:")
print(dataExclude,"\n")
