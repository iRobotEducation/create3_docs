'''
BSD 3-Clause License

Copyright (c) 2022, Rudis Laboratories
Additions Copyright (c) 2022 iRobot Corporation
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Requires mkdocs-macros-plugin:
pip3 install mkdocs-macros-plugin

listfiles() function used in:
print_compute.md
print_casters.md
print_generic.md
print_sensor_mounts.md

Generates in those files a 3D viewable tree structure of model files.

Set env.variables['branch'] to the branch with your updated file structures pushed, ex: "jinja-ninja".
Set env.variables['org'] to your github organization name, ex: "rudislabs".
Set env.variables['render_size_limit'] to max size in kB of stl file for 3D viewing, if above set size include a png image in file structure for viewer to use.

Currently using details in local .git to generate branch and org names.
'''
import os

# Begining of optional block and can be commented out if setting variables manually
from git import Repo 
repo = Repo(os.getcwd())
assert not repo.bare
currentGitOrg = repo.remotes.origin.url.split('.git')[0].replace('git@github.com:','').replace('https://github.com/','').split('/')[-2]
currentGitBranch = repo.active_branch.name
print('INFO\t -  Using github organization in main.py: {:s}'.format(currentGitOrg))
print('INFO\t -  Using git branch in main.py: {:s}'.format(currentGitBranch))
# End of optional block


def define_env(env):
    env.variables['branch'] = currentGitBranch
    env.variables['org'] = currentGitOrg
    env.variables['render_size_limit'] = "5000"

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
                        # Switch to using MB if above 500 kB
                        fileSize_str=f"{fileSize/1000.0:.2f} MB"
                    while path != os.path.dirname(root_str):
                        # Replace underscores in file folders with spaces, this creates the ToC tree.
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
