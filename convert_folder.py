from os import listdir
import os.path
from url_convert import url_conv

def convert(dn):
    for filename in listdir(dn):
        if ".url" in filename:
            with open(os.path.join(dn, filename)) as f:
                for line in f.readlines():
                    if line.lower().startswith("url="):
                        url_conv(line[4:].strip(), os.path.join(dn, filename.replace(".url", "")))
            
convert(r"C:\Users\suzur\Google Drive\UCI\Junior 1Q\CS 122A")