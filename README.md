# 1. 确保系统安装了python

#2 .get_upload_files.py
 ##获取需要上传到服务器上的文件列表，并保存到指定的文件夹
 
#源文件的目录  
##fromdir = "source_folder"
#根据filelist.txt 复制的文件存储目录
##todir = "backup"
#需要上传服务器的文件列表
##filename = 'filelist.txt'
   
#3.backup_server_files.py
##备份目录文件
  todir = "backup"
##需要备份的文件列表
  filename = 'filelist.txt'
### 服务器的代码路径，记住最后的 / 需要保留  
  SRC_FOLDER = ‘/path_to_server_src_folder/‘
    

#4.filelist.txt 这个文件存储需要上传的文件
###git如何获取需要上传的文件
<pre>
<code>
  git diff --name-status HEAD~2 HEAD~3
  git diff <commit> <commit>
  git diff b45ba47d1b297217e3ec6a3ab0f61716a8d6ecbc c244d0bf06d56ec86aaedeefa5dcd84dd9febc60
一般来说，通过 hash 串的前 4～6 位就可以区分，所示可以简写为：
  git diff b45b 355e
</code>
</pre>
###svn 如何获取2个版本之前差异
http://www.cnblogs.com/QLeelulu/archive/2009/12/09/1619927.html
