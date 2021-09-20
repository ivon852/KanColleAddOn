import glob
import os

def list_textures_v2():
  for texture in glob.glob("./textures/**/*.png")+glob.glob("./textures/**/*.tga"):
    bn = os.path.splitext(os.path.basename(texture))[1]
    print('"'+texture.replace(bn,"").replace("./","").replace("\\","/")+'",')



list_textures_v2()