# REQUIREMENTS 

Requires Python 3.4 or later to work

# HOW TO INSTALL

Download or Clone the code and run the **bat** file.
And **Tadaaa**

# HOW DOES IT WORK

The symfony installer script is a simple bat file with multiple python scripts is made to ease symfony installation. 
The scripts follows these steps to finish :

* Install the required python libraries 
* Check **git** is installed and install it if not using **winget**
* Istall **powershell scoop** if didn't exist 
* Download and install **php 8.1** and add it automatically to **the path** if it didn't find any php version
* Download and install **php composer**
* Finally it installs **symfony**

And that is it.

## To check if symfony installed : 
* Open **CMD** and input
```shell
symfony new project
```
**BUG** : if symfony not installed, open **windows powershell** and input 
```shell
scoop install symfony-cli
```
**Thank you for using this script**

**Feel free to tell me what did you think about it and how I can improve**

**HAVE A LOVELY DAY**
