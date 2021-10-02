#elete comma
from os import walk
import os
from os.path import join

mypath = "./"
filename="contents.json"

if not os.path.isfile(filename):
 fp = open(filename, "w")
 fp.write('{"content":[')
 for root, dirs, files in walk(mypath):
  for f in files:
   fullpath = join(root, f)
   fp.write( '{"path":"' + fullpath.replace("./","").replace('\\',"/") + '"},')
 fp.write('],"version":1}')
 fp.close()