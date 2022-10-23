import subprocess as sp
import os


output = sp.getoutput('git -v')

print("checking git")
if output.find("pas reconnu")>0 or output.find("is not recognized")>0:
    print("installing git...")
    os.system('cmd /k winget install --id Git.Git -e --source winget')

else:
    print(output)

print("git is ready")