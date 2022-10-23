from pathlib import Path
from pyuac import main_requires_admin
import requests
import os,sys
import subprocess as sp

link = "https://getcomposer.org/Composer-Setup.exe"
output_path = str(Path.home() / "Downloads")

file_name=output_path+"/Composer-Setup.exe"

@main_requires_admin
def main():
    # downloading composer
    print("Downloading composer.")
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
    print("installing file... ")
    os.system(file_name)
    print("installing done.")

    input("Press enter to close the window. >")

if __name__ == "__main__":
    main()
