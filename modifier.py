import os
import re

rootdir = 'C:/Users/Brandon/DirectoryOrganizer/testDir'

def main():
  for root, dirs, files in os.walk(rootdir):
    if(len(dirs)>0):
      continue 

    rootName = getParentName(root)
    if(len(files)>1):
      index = 1
      for singleFile in files:
        fileExt = getFileExt(singleFile)
        newPath = getFilePath(rootName, fileExt, str(index))
        oldPath = getOldFilePath(root, singleFile, fileExt)
        renameFiles(oldPath, newPath)
        index += 1
    else:
      fileExt = getFileExt(files[0])
      newPath = getFilePath(rootName, fileExt)
      oldPath = getOldFilePath(root, files[0], fileExt)
      renameFiles(oldPath, newPath)
    removeOldDir(root)

  print("done")

def removeOldDir(rootPath:str) -> str:
  os.rmdir(rootPath)

def getOldFilePath(rootPath:str, fileName:str, ext:str) -> str:
  return rootPath + '/' + fileName 

def renameFiles(oldPath:str, newPath:str) -> None:
  print(oldPath + ' -> ' + newPath)
  os.rename(oldPath, newPath)

def getFilePath(rootName:str, fileExt:str, index:str='') -> str:
  return rootdir + '/' + rootName + index + '.' + fileExt

def getFileExt(fileName:str) -> str:
  return fileName.split('.')[1]

def getParentName(root:str) -> str:
  roots = re.split(r'\\|/', root)
  return roots[len(roots)-1]

if __name__ == "__main__":
  main()