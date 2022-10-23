
import subprocess as sp

print("installing symfony...")
sp.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe scoop install symfony-cli', shell=True)

print('symfony intalled.')