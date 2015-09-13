#!/usr/bin/python
import os 
import os.path 
import shutil 
import time,  datetime
import string 

todir = "backup"
filename = 'filelist.txt'
SRC_FOLDER = '/path_to_server_file_dir/'

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
    not_exist_count =0;
    folder_array =[]
    not_exist_array = []
    print("current_path "+ current_path )
    if not os.path.exists(os.path.join(current_path, todir) ):  
                os.makedirs(os.path.join(current_path, todir) )  
    for line in text_file:
       line=line.strip('\n')
       line=line.strip('\r')
       #filelist.txt 里需要替换的前面部分
       ltrip_str = "/source_folder/"
       line = line.replace(ltrip_str, '')
       
       srcFile = SRC_FOLDER + line;
       dstFile = current_path + '/' + todir +"/" +line
       
       print("srcFile " +srcFile)
       print ("dstFile %s "%dstFile)
       
       targetDir = os.path.dirname(dstFile)
       
       if os.path.isdir(srcFile): 
          folder_count = folder_count+1
          print("srcFile is floder %s"%srcFile)
          folder_array.append(line)
          continue;
          
       if not os.path.exists(srcFile) :
          not_exist_count = not_exist_count+1
          not_exist_array.append(line)
          continue
          

       if not os.path.exists(targetDir):  
              os.makedirs(targetDir)  
       print("cp "+ srcFile +" to " + dstFile)
       cpFile(srcFile,dstFile)
       all_line  = all_line + 1
       
    print('----------------------------')  
    print('') 
    print('') 
    print('----------not_exist_array------------------')  
    
    for line in not_exist_array:
        print (line)
        
    print('') 
    print('') 
    print('-----------------folder_array ----------------------------')  
    for line in folder_array:
        print (line)   
        
    print('') 
    print('')    
    
    print('----------- result -----------------')      
    print ("copy success  file : %d folder: %d not exist: %d"  % (all_line,folder_count,not_exist_count))
  
    