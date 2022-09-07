"""
If you're reading this trying to figure out how the files got auto-generated in
mkdocs... I'm sorry, take a break, re-evaluate your life and don't forget to 
pip install mkdocs-macros-plugin
"""

import os

def define_env(env):
    @env.macro
    def listfiles(path):
        fileDetails={}
        for root, dirs, files in os.walk(path, topdown=False):
            dirs.sort()
            for file in files:
                if ".stl" in file:
                    dirDepth=[]
                    root_str=os.path.join(root,file)
                    fileSize=float(os.path.getsize(os.path.join(root,file)))/1000.0
                    fileSize_str=f"{int(fileSize):d} kB"
                    if fileSize > 500:
                        fileSize_str=f"{fileSize/1000.0:.2f} MB"
                    while path != os.path.dirname(root_str):
                        dirDepth.append(os.path.basename(os.path.dirname(root_str)).replace('_',' '))
                        root_str=os.path.dirname(root_str)
                        
                    entry={"name": file,
                        "path": root.replace('docs/',''),
                        "size_str": fileSize_str,
                        "size_raw_kb": str(fileSize),
                        "extension": "stl"}
                    
                    if len(dirDepth) == 1:
                        if dirDepth[0] not in fileDetails:
                            fileDetails.update({dirDepth[0]:{}})
                        fileDetails[dirDepth[0]].update(entry)
                    if len(dirDepth) == 2:
                        if dirDepth[1] not in fileDetails:
                            fileDetails.update({dirDepth[1]:{dirDepth[0]:{}}})
                        if dirDepth[0] not in fileDetails[dirDepth[1]]:
                            fileDetails[dirDepth[1]].update({dirDepth[0]:{}})
                        fileDetails[dirDepth[1]][dirDepth[0]].update(entry)
                    if len(dirDepth) == 3:
                        if dirDepth[2] not in fileDetails:
                            fileDetails.update({dirDepth[2]:{dirDepth[1]:{dirDepth[0]:{}}}})
                        if dirDepth[1] not in fileDetails[dirDepth[2]]:
                            fileDetails[dirDepth[2]].update({dirDepth[1]:{dirDepth[0]:{}}})
                        if dirDepth[0] not in fileDetails[dirDepth[2]][dirDepth[1]]:
                            fileDetails[dirDepth[2]][dirDepth[1]].update({dirDepth[0]:{}})
                        fileDetails[dirDepth[2]][dirDepth[1]][dirDepth[0]].update(entry)
        return fileDetails
