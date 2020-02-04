
# turkish-deasciifier: Turkish deasciifier

This is a **deasciifier** Python library and command line utility for Turkish that solves the problem of **diacritics restoration** (also known as **diacritics reconstruction**). It takes a Turkish string containing only
ASCII characters (that is, without proper diacritics) and replaces the relevant characters with their corresponding
Turkish letters.

The web-based, online version of this system is available at:

http://turkceyap.appspot.com/

Keep in mind that diacritics restoration (deasciification) for Turkish doesn't work 100% of the time; it is an active research topic! Still, this library is good enough for many practical purposes, and served many people and projects in the last 10 years.

This system is based on the [turkish-mode](http://github.com/emres/turkish-mode) for [GNU Emacs](https://www.gnu.org/software/emacs/) by [Prof. Deniz Yüret](http://www.denizyuret.com/).

# Table of Contents
1. [Installation](#installation)
2. [Example Python Library Usage](#example-python-library-usage)
3. [Example CLI (Command Line Interface) Usage](#example-cli-command-line-interface-usage)
4. [Other Programming Languages and Systems](#other-programming-languages-and-systems)
5. [Advanced Research](#advanced-research)

## Installation
### Python 3
For now, the recommended way to install is to use [pip](https://pypi.org/project/pip/) and install direcly from the GitHub repository:

```shell
pip install git+https://github.com/emres/turkish-deasciifier.git
```

### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)! If you insist on using Python 2.x, you can install using the following command:

```shell
pip install Turkish-Deasciifier
```

## Example Python Library Usage
### Python 3
```python
from turkish.deasciifier import Deasciifier

my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
deasciifier = Deasciifier(my_ascii_turkish_txt)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print(my_deasciified_turkish_txt)
```

### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)! If you insist on using Python 2.x, you can use the library in the following manner: 

```python
from turkish.deasciifier import Deasciifier

my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
deasciifier = Deasciifier(my_ascii_turkish_txt.decode("utf-8"))
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print my_deasciified_turkish_txt.encode("utf-8")
```		


### Example CLI (Command Line Interface) Usage
#### Python 3
Example tested in a Bash shell:

```shell
$ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify
$ cat somefile.txt | turkish-deasciify
```

#### Python 2
Keep in mind that [switching to Python 3 is strongly recommended](https://www.python.org/doc/sunset-python-2/)!

Example tested in a Bash shell:

```shell
$ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify-python2
$ cat somefile.txt | turkish-deasciify-python2
```

### Other Programming Languages and Systems

* Java: [https://github.com/ahmetb/turkish-deasciifier-java](https://github.com/ahmetb/turkish-deasciifier-java)
* Perl: [https://metacpan.org/pod/release/BURAK/Lingua-TR-ASCII-0.13/lib/Lingua/TR/ASCII.pm](https://metacpan.org/pod/release/BURAK/Lingua-TR-ASCII-0.13/lib/Lingua/TR/ASCII.pm)
* Haskell:  [http://hackage.haskell.org/package/turkish-deasciifier](http://hackage.haskell.org/package/turkish-deasciifier)
* Node.js: [https://github.com/f/deasciifier/](https://github.com/f/deasciifier/)
* VIM: [https://github.com/joom/turkish-deasciifier.vim](https://github.com/joom/turkish-deasciifier.vim)
* Emacs Lisp: [https://github.com/emres/turkish-mode](https://github.com/emres/turkish-mode) (also available as a [package in MELPA](https://melpa.org/#/turkish))

## Advanced Research
For recent advanced scientific research articles, please see the following:

* Diacritics Restoration Using Neural Networks
    * Paper: [https://www.aclweb.org/anthology/L18-1247.pdf](https://www.aclweb.org/anthology/L18-1247.pdf)
    * Code: [https://github.com/arahusky/diacritics_restoration](https://github.com/arahusky/diacritics_restoration)
    * Data sets: [Corpus for training and evaluating diacritics restoration systems](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2607)
* Diacritic restoration of Turkish tweets with word2vec
    * Paper: [https://www.sciencedirect.com/science/article/pii/S2215098618308668](https://www.sciencedirect.com/science/article/pii/S2215098618308668)
