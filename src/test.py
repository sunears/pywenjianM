#!/usr/bin/python
import sys
import time
import os
import os.path,shutil
import glob
import calendar
def renameIt(strDirector):
    rootDir=strDirector
    for parent,dirnames,filenames in os.walk(rootDir):
        for filename in filenames:
            print rootDir+filename
            statInfo=os.stat(rootDir+filename)
            print time.strftime('%Y%m%d_%H%M%S', time.localtime(statInfo.st_mtime))
    return
def renameItTwo(strDirector):
    rootDir=strDirector
    os.chdir(rootDir)
    for filename in glob.glob("*.TOD"):
        print filename
        filenameArray=os.path.splitext(filename)
        print filenameArray[0]
        statInfo=os.stat(filename)
        timeName=time.strftime('%Y%m%d_%H%M%S', time.localtime(statInfo.st_mtime))
        print time.strftime('%Y%m%d_%H%M%S', time.localtime(statInfo.st_mtime))
        print os.path.exists(filenameArray[0]+".mov")
        if os.path.exists(filenameArray[0]+".mov"):
            os.rename(filenameArray[0]+".mov",filenameArray[0]+"_"+timeName+".mov")
            print "os.rename"+filenameArray[0]+".mov"+filenameArray[0]+"_"+timeName+".mov"
    return
def toDir(strDirector):
    os.chdir(strDirector)
    prefix="HUGE"
    arrayPrefix=["HUGE","ALL_SYS","all_magic","ALL_ITEM","ALL_CHAR","ALL_MAP1","ALL_MAP2"]
    for prefix in arrayPrefix:
        mkDirAndMovFiles(prefix)
    return
def mkDirAndMovFiles(wantDirName):
    if not os.path.exists(wantDirName):
        os.mkdir(wantDirName)
    for filename in glob.glob(wantDirName+"*"):
        if not os.path.isdir(filename):
            shutil.move(filename,wantDirName+"\\"+filename)  
    return
def createFilesToTest(path):
    if(os.path.exists(path)):
        print path+"exists"
        c=calendar.Calendar()
        print type(c.itermonthdates(2015, 12))
    return
s=len(sys.argv)
if s>1:
    #toDir(s[1])
    print sys.argv[s-1]
    #toDir(sys.argv[s-1])
else:
    print s

createFilesToTest("./")

