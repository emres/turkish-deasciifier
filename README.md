
# turkish-deasciifier: Turkish deasciifier

This is a **deasciifier** Python library and command line utility for Turkish that solves the problem of **diacritics restoration** (also known as **diacritics reconstruction**). It takes a Turkish string containing only
ASCII characters (that is, without proper diacritics) and replaces the relevant characters with their corresponding
Turkish letters.

The web-based, online version of this system is available at:

~~http://turkceyap.appspot.com~~ (I'm currently too busy to fix it, please use https://deasciifier.com/ instead!)

Keep in mind that diacritics restoration (deasciification) for Turkish doesn't work 100% of the time; it is an active research topic! Still, this library is good enough for many practical purposes, and served many people and projects in the last 15 years.

This system is based on the [turkish-mode](http://github.com/emres/turkish-mode) for [GNU Emacs](https://www.gnu.org/software/emacs/) by [Prof. Deniz Yüret](http://www.denizyuret.com/).

# Table of Contents
1. [Installation](#installation)
2. [Example Python Library Usage](#example-python-library-usage)
3. [Example CLI (Command Line Interface) Usage](#example-cli-command-line-interface-usage)
4. [Other Programming Languages and Systems](#other-programming-languages-and-systems)
5. [Advanced Research](#advanced-research)

## Installation

Requires **Python 3.11+**. Works on all platforms (Linux, macOS Intel & Apple Silicon, Windows).

Install from the project root using [pip](https://pypi.org/project/pip/) (PEP 517 build):

```shell
pip install .
```

Or install directly from GitHub:

```shell
pip install git+https://github.com/emres/turkish-deasciifier.git
```

Editable install for development:

```shell
pip install -e .
```

## Example Python Library Usage

```python
from turkish.deasciifier import Deasciifier

my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
deasciifier = Deasciifier(my_ascii_turkish_txt)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print(my_deasciified_turkish_txt)
```

Or use the package shorthand:

```python
from turkish import Deasciifier
```		


### Example CLI (Command Line Interface) Usage

After installation, the `turkish-deasciify` command is available:

```shell
$ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify
$ cat somefile.txt | turkish-deasciify
```

You can also run the module directly: `python -m turkish`

### Running tests

```shell
python -m unittest tests
```

### Other Programming Languages and Systems

* Java: [https://github.com/ahmetb/turkish-deasciifier-java](https://github.com/ahmetb/turkish-deasciifier-java)
* Perl: [https://metacpan.org/pod/release/BURAK/Lingua-TR-ASCII-0.13/lib/Lingua/TR/ASCII.pm](https://metacpan.org/pod/release/BURAK/Lingua-TR-ASCII-0.13/lib/Lingua/TR/ASCII.pm)
* Haskell:  [http://hackage.haskell.org/package/turkish-deasciifier](http://hackage.haskell.org/package/turkish-deasciifier)
* Node.js: [https://github.com/f/deasciifier/](https://github.com/f/deasciifier/)
* VIM: [https://github.com/joom/turkish-deasciifier.vim](https://github.com/joom/turkish-deasciifier.vim)
* Emacs Lisp: [https://github.com/emres/turkish-mode](https://github.com/emres/turkish-mode) (also available as a [package in MELPA](https://melpa.org/#/turkish))
* Swift: [https://github.com/armish/TurkishDeasciifier](https://github.com/armish/TurkishDeasciifier)

## Advanced Research
For recent advanced scientific research articles, please see the following:

* [The Deceptively Complex World of Turkish Diacritics: A Neural Network Journey](https://ergoso.me/turkish/neural/network/github/diacritics/macos/app/swift/python/2025/09/17/turkish-diacritic-restoration.html)
    * [https://github.com/armish/nokta-ai](https://github.com/armish/nokta-ai)
* Diacritic Restoration Using Recurrent Neural Network
    * Paper: https://github.com/aysnrgenc/TurkishDeasciifier/blob/master/diacritic-restoration-recurrent.pdf
    * Code: https://github.com/aysnrgenc/TurkishDeasciifier
    * Data sets: https://github.com/aysnrgenc/TurkishDeasciifier/tree/master/data
* Diacritics Restoration Using Neural Networks
    * Paper: [https://www.aclweb.org/anthology/L18-1247.pdf](https://www.aclweb.org/anthology/L18-1247.pdf)
    * Code: [https://github.com/arahusky/diacritics_restoration](https://github.com/arahusky/diacritics_restoration)
    * Data sets: [Corpus for training and evaluating diacritics restoration systems](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2607)
* Diacritic restoration of Turkish tweets with word2vec
    * Paper: [https://www.sciencedirect.com/science/article/pii/S2215098618308668](https://www.sciencedirect.com/science/article/pii/S2215098618308668)
* Vowel and Diacritic Restoration for Social Media Texts
    * Paper: [https://www.aclweb.org/anthology/W14-1307/](https://www.aclweb.org/anthology/W14-1307/)
    * Full text (PDF): [https://www.aclweb.org/anthology/W14-1307.pdf](https://www.aclweb.org/anthology/W14-1307.pdf)
    * Web demo: [http://tools.nlp.itu.edu.tr/Deasciifier](http://tools.nlp.itu.edu.tr/Deasciifier)
