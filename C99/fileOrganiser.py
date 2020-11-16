import os
import shutil

# Write the name of the directory here,
# that needs to get sorted
# path = '/home/rajeev/Videos'
path = input("enter the name of the directory to be sorted :- ")

# This will create a properly organized
# list with all the filename that is
# there in the directory
list_of_files = os.listdir(path)

# This will go through each and every file
for file in list_of_files:
    
    name, ext = os.path.splitext(file) # declaring two variables name, ext to extract the data
    # os.path.splitext(file) returns tuple data type
    print(ext)
    #https://www.w3schools.com/python/python_tuples.asp
    
    # thistuple = ('.txt'), 
    #print(thistuple[1:]) -> returns txt, where as print(thistuple[0:]) returns .txt

    # This is going to store the extension type
    ext = ext[1:] 


    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue

    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    # This will create a new directory,
    # if the directory does not already exist
    else:
        # os.makedirs will create other folders the path if they dont exist
        #os.makedirs() method in Python is used to create a directory recursively. 
        #That means while making leaf directory if any intermediate-level directory is missing, 
        #os.makedirs() method will create them all.
        #For example consider the following path:

#/home/User/Documents/GeeksForGeeks/Authors/ihritik
#Suppose we want to create directory ‘ihritik’ but Directory ‘GeeksForGeeks’ 
#and ‘Authors’ are unavailable in the path. 
#Then os.makedirs() method will create all unavailable/missing directory in the specified path.
# ‘GeeksForGeeks’ and ‘Authors’ will be created first then ‘ihritik’ directory will be created.
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)