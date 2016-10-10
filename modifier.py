import os
import re

def main():
  rootdir = 'd:/Users/brandon.runyan/fileModifier'
  for root, dirs, files in os.walk(rootdir):
    print(root)
    if(len(dirs)>0):
      continue 
    if(len(files)>1):
      for file in files:
        index = 1
        print(getParentName(root) + str(index))
        index += 1

  print("done")

def getParentName(root:str) -> str:
  roots = re.split(r'\\|/', root)
  return roots[len(roots)-1]

if __name__ == "__main__":
  main()