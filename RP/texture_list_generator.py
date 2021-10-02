#Delete comma
import glob
import os

filename="./textures/texture_list.json"
if not os.path.isfile(filename):
 fp = open(filename, "w")
 fp.write('[');
 for texture in glob.glob("./textures/**/*.png")+glob.glob("./textures/**/*.tga")+glob.glob("./subpacks/kanmusu_subpack/textures/**/*.tga")+glob.glob("./subpacks/kanmusu_subpack/textures/**/*.png"):
  bn = os.path.splitext(os.path.basename(texture))[1]
  fp.write('"'+texture.replace(bn,"").replace("./","").replace("\\","/").replace("subpacks/kanmusu_subpack/","")+'",')
 fp.write(']')
 fp.close()