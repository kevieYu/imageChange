#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Add the picture name wiht "@ 2 x" ,put the pictures of the two images into a three times.

import sys, getopt
import os
from PIL import Image
import re

def main(argv):
       inputDir = ''
       try:
          opts, args = getopt.getopt(argv,"hi:",["ifile="])
       except getopt.GetoptError:
          print ('test.py -i <inputDir>')
          sys.exit(2)
       for opt, arg in opts:
          if opt == '-h':
             print ('test.py -i <inputDir>')
             sys.exit()
          elif opt in ("-i", "--ifile"):
             inputDir = arg
             if not os.path.isdir(inputDir):
                    print ('文件夹不存在')
                    sys.exit()
             return os.path.abspath(inputDir)

if __name__ == "__main__":
        path = main(sys.argv[1:])
        for name in [x for x in os.listdir(os.chdir(path)) if os.path.isfile(x) and os.path.splitext(x)[1]=='.png']:
            if '2x' not in name and '3x' not in name:
                nameList = name.split('.')
                # nameList[0]+'@2x'+nameList[1]
                print(nameList[0]+'@2x.'+nameList[1])
                os.renames(name, nameList[0]+'@2x.'+nameList[1])
        for name in [x for x in os.listdir(os.chdir(path)) if os.path.isfile(x) and os.path.splitext(x)[1]=='.png']:
            if  '2x' in name:
                infile = path+'/'+name
                im = Image.open(infile)
            #    print(im.format,im.size,im.mode)
                w, h = im.size
                out = im.resize((w*150//100, h*150//100),Image.ANTIALIAS)
                strinfo = re.compile('2x')
                b = strinfo.sub('3x',infile)
                out.save(b, 'png')
                print(name)
        print('完成')
