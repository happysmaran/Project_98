def swapFileData():
    file1=input("Enter First File Name To Swap: ")
    file2=input("Enter Second File Name To Swap: ")

    fileread1=open(file1, 'r')
    fileread2=open(file2, 'r')
    data_a=fileread1.read()
    data_b=fileread2.read()
    
    filewrite1=open(file1, 'w')
    filewrite2=open(file2, 'w')
    
    filewrite1.write(data_b)
    filewrite2.write(data_a)

swapFileData()
print('done')
