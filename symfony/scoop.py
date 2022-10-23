import subprocess as sp

print('Installing scoop...')
sp.call("C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe iex (new-object net.webclient).downloadstring('https://get.scoop.sh')", shell=True)
print("scoop installed...")

