from pathlib import Path
from pyuac import main_requires_admin
import requests
import os,sys
import subprocess as sp


link = "https://windows.php.net/downloads/releases/php-8.1.11-nts-Win32-vs16-x64.zip"
output_path = str(Path.home() / "Downloads")

file_name=output_path+"/php-8.1.11-nts-Win32-vs16-x64.zip"

@main_requires_admin
def main():
    # downloading php
    print("Downloading php.")
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
    print("download finished.")
    print("Extracting file... ")
    sp.call("C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe Expand-Archive -LiteralPath "+output_path+"/php-8.1.11-nts-Win32-vs16-x64.zip -DestinationPath 'C:/Program Files/php-8.1.11-nts-Win32-vs16-x64'", shell=True)
    print("Extracting done.")

    
    print('Adding php to path...')

    os.system('cmd /c setx /m PATH "%PATH%C:\Program Files\php-8.1.11-nts-Win32-vs16-x64"')

  
    print("php to path added.") 


if __name__ == "__main__":
    path  = sp.getoutput('path')
    print(path)
    if path.find("php-8")>0:
        print("Php is installed. Bye !")
    else:
        main()
