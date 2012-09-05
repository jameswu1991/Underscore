import glob
import os.path
import sys
import warnings

from nose import tools as nt
from underscore import _

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def testGenerator():
    if not os.path.isdir('examples/underscored'):
        os.mkdir('examples/underscored')
    for filename in glob.glob('examples/*.py'):
        # Python 2.6 Compat
        if ('2.7' not in filename or 
            ('2.7' in filename and sys.version_info >= (2,7))):
            yield _testFile, filename


def _testFile(original_file):
    underscored_file = os.path.join('examples', 'underscored', 
                               os.path.basename(original_file))
    _(original_file, underscored_file, original=True)
    expected_output = _execute(original_file)
    actual_output = _execute(underscored_file)
    nt.assert_equal(actual_output, expected_output)

def _execute(filename):
    sys.stdout = fileOut = StringIO()
    with open(filename) as python_file:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            exec(python_file.read(), {})
    sys.stdout = sys.__stdout__
    output = fileOut.getvalue()
    fileOut.close()
    return output
