pip install pathlib
pip install requests
pip install pyuac
pip install pywin32
start /w python "%cd%/symfony/git.py" & python "%cd%/symfony/scoop.py" & python "%cd%/symfony/php.py" & python "%cd%/symfony/composer.py" & python "%cd%/symfony/symfony.py"

@pause