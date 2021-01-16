import gzip
import xml.etree.ElementTree as ET
import shutil
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
subname = filename.split('.sub')[0]
shutil.copyfile(filename, filename + '.bkp') #make a backup just in case...

#node removal
def node_remove(root):
    #find all wires containing nodes
    for Item in root.findall("./Item/Wire[@nodes]"):
    #nodes string to list
        x = Item.get('nodes').split(';')
    #take only the first and last pairs
        y = [x[0],x[1],x[-2],x[-1]]
        z = ';'.join(y)
    #replace attribute with modified string
        Item.set('nodes', z)
    return root

#open gzip file and remove nodes
with gzip.open(filename, 'r') as f:
    tree = ET.parse(f)
    root = node_remove(tree.getroot())

#compress file
with gzip.open(subname, 'wb') as f:
    tree.write(f)

#cleanup        
shutil.copy(subname, filename)
os.remove(subname)
