#!/usr/bin/python
import os 
import os.path 
import shutil 
import time,  datetime
import string 

fromdir = "source_folder"
todir = "backup"
filename = 'filelist.txt'

#
def cpFile(srcPath, destPath):  
    shutil.copy(srcPath,destPath)
    #shutil.copytree(srcPath,destPath) 
#  
def copyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".svn") > 0: 
        return 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                    open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)
#            
if  __name__ == "__main__":
    text_file = open("./"+filename ,"r")
    #current_path = os.getcwd() 
    current_path = os.getcwd() 
    all_line = 0
    folder_count = 0;
    print("current_path "+ current_path )
    if not os.path.exists(os.path.join(current_path, todir) ):  
                os.makedirs(os.path.join(current_path, todir) )  
    for line in text_file:
       line=line.strip('\n')
       srcFile = current_path + line
       dstFile = current_path + '/' + todir + line
       targetDir = os.path.dirname(dstFile)
       if not os.path.isfile(srcFile): 
          folder_count = folder_count+1
          continue;
       print (srcFile)
       print (dstFile)
       if not os.path.exists(targetDir):  
              os.makedirs(targetDir)  
       print("cp "+ srcFile +" to " + dstFile)
       cpFile(srcFile,dstFile)
       all_line  = all_line + 1
       
    print ("copy success  file : %d folder: %d" % (all_line,folder_count))
  
    