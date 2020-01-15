
# turkish-deasciifier: Turkish deasciifier

This is a **deasciifier** Python library and command line utility for Turkish that solves the problem of **diacritics restoration**. It takes a Turkish string containing only
ASCII characters (that is, without proper diacritics) and replaces the relevant characters with their corresponding
Turkish letters.

The web-based, online version of this system is available at:

http://turkceyap.appspot.com/

Keep in mind that diacritics restoration (deasciification) for Turkish doesn't work 100% of the time; it is an active research topic! Still, this library is good enough for many practical purposes, and served many people and projects in the last 10 years.

This system is based on the [turkish-mode](http://github.com/emres/turkish-mode)
by [Prof. Deniz Yüret](http://www.denizyuret.com/).

## Installation
### Python 3
For now, the recommended way to install is to use [pip](https://pypi.org/project/pip/) and install direcly from the GitHub repository:

    pip install git+https://github.com/emres/turkish-deasciifier.git
    
### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)! If you insist on using Python 2.x, you can install using the following command:

    pip install Turkish-Deasciifier

## Example Python Library Usage
### Python 3

		from turkish.deasciifier import Deasciifier

		my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
		deasciifier = Deasciifier(my_ascii_turkish_txt)
		my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
		print(my_deasciified_turkish_txt)
### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)! If you insist on using Python 2.x, you can use the library in the following manner: 

		from turkish.deasciifier import Deasciifier

		my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
		deasciifier = Deasciifier(my_ascii_turkish_txt.decode("utf-8"))
		my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
		print my_deasciified_turkish_txt.encode("utf-8")
		


### Example CLI (Command Line Interface) Usage
#### Python 3
Example tested in a Bash shell:

		$ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify
		$ cat somefile.txt | turkish-deasciify

#### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)!

Example tested in a Bash shell:

		$ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify-python2
		$ cat somefile.txt | turkish-deasciify-python2

