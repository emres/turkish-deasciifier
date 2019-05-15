# -*- coding: utf-8 -*-

"""
Setup file for deasciifier.
This file is in public domain.
"""

# -----------------------------------------------------------------------------
# Bundle
# -----------------------------------------------------------------------------

CMDCLASS = {}

from distutils.core import Command
from os.path import join as pjoin
import os, sys
import unittest
import tests

class TestCommand(Command):
    """
    New distutils command for unit tests.
    """
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """
        run tests
        """
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(tests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if result.errors or result.failures:
            raise SystemExit("")

CMDCLASS['test'] = TestCommand

from distutils.command.clean import clean as Clean

class CleanCommand(Clean):
    """
    Command to remove cruft.
    Enhanced clean command to remove extra cruft.
    """
    def run(self):
        """clean compiled files"""
        Clean.run(self)
        for root, _, files in os.walk(os.curdir):
            for f in files:
                if f.endswith('.pyc') or f.endswith('.pyo'):
                    p = pjoin(root, f)
                    try:
                        os.unlink(p)
                    except OSError as e:
                        print('could not clean %r: %s' % (p, e), file=sys.stderr)

CMDCLASS['clean'] = CleanCommand

try:# Check command is optional.
    # Mute pylint: disable-msg=E0611
    from pyflakes.checker import Checker as FlakeChecker
    import compiler

    def check(code_string, filename):
        """check a code string"""
        try:
            tree = compiler.parse(code_string)
        except (SyntaxError, IndentationError):
            value = sys.exc_info()[1]
            try:
                (lineno, offset, line) = value[1][1:]
            except IndexError:
                print('could not compile %r' % (filename,), file=sys.stderr)
                return 1
            if line.endswith("\n"):
                line = line[:-1]
            print('%s:%d: could not compile' % (filename, lineno), file=sys.stderr)
            print(line, file=sys.stderr)
            print(" " * (offset-2), "^", file=sys.stderr)
            return 1
        else:
            import locale
            try:
                locale.setlocale(locale.LC_ALL, 'C')
            except locale.Error as e:
                print('setlocale failed: %s' % (e,), file=sys.stderr)
            w = FlakeChecker(tree, filename)
            w.messages.sort(lambda a, b: cmp(a.lineno, b.lineno))
            for warning in w.messages:
                print(warning)
            return len(w.messages)

    def check_path(filename):
        """check code in a path"""
        if os.path.exists(filename):
            return check(file(filename, 'U').read(), filename)

    def run_flake():
        """run flake over the whole directory"""
        warnings = 0

        for root, _, files in os.walk(os.curdir):
            for f in files:
                if f.endswith('.py'):
                    warnings += check_path(os.path.join(root, f))
        raise SystemExit(warnings > 0) # pylint: disable-msg=W1010

    class CheckCommand(Command):
        """
        New distutils command to check code with Pyflakes.
        """
        user_options = []

        def initialize_options(self):
            """init options"""
            pass

        def finalize_options(self):
            """finalize options"""
            pass

        def run(self):
            """check code with Pyflakes"""
            run_flake()

    CMDCLASS['check'] = CheckCommand
except ImportError:
    print("couldn't found Pyflakes", file=sys.stderr)


# ----------------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------------

from distutils.core import setup
setup(
    cmdclass         = CMDCLASS,
    name             = 'Turkish Deasciifier',
    description      = 'deasciify a given Turkish text',
    long_description = 'This class helps to deasciify Turkish texts. If a Turkish text is written using only ASCII letters, that is not including any Turkish letters, then by using the methods of this class it is possible to convert that text into a correct form, that includes corresponding Turkish letters. It cannot do this perfectly but works most of the time.',
    version          = '0.1',
    author           = 'Emre Sevinç',
    author_email     = 'emre.sevinc@gmail.com',
    license          = 'Public Domain',
    url              = 'http://github.com/emres/turkish-deasciifier',
    keywords         = ('turkish', 'deasciifier'),
    platforms        = 'any',
    packages         = ['turkish'],
    scripts          = ['turkish-deasciify'],
)
