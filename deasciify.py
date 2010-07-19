import sys
import deasciifier

class Deasciify:
    """
    This is the commandline utility for deasciification.

    Example usage:

    $ echo "Opusmegi cagristiran catirtilar." | python deasciify.py
    $ cat somefile.txt | python deasciify.py
    """


    def deasciify(self):
        string = sys.stdin.read()
        dea = deasciifier.Deasciifier(string.decode("utf-8"))
        result = dea.convert_to_turkish()
        sys.stdout.write(result.encode("utf-8"))

d = Deasciify()
d.deasciify()
