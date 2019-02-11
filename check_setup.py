import sys
import os
from distutils.version import LooseVersion

if sys.version_info.major < 3:
    print('[!] You are running an old version of Python. '
          'This tutorial requires Python 3.')

    sys.exit(1)

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    reqs = f.readlines()

reqs = [(pkg, ver) for (pkg, _, ver) in
        (req.split() for req in reqs if req.strip())]

pkg_names = {
    'scikit-image': 'skimage',
    'scikit-learn': 'sklearn'
}

for (pkg, version_wanted) in reqs:
    module_name = pkg_names.get(pkg, pkg)
    try:
        m = __import__(module_name)
        status = '✓'
    except ImportError as e:
        m = None
        if (pkg != 'numpy' and 'numpy' in str(e)):
            status = '?'
            version_installed = 'Needs NumPy'
        else:
            version_installed = 'Not installed'
            status = 'X'

    if m is not None:
        version_installed = m.__version__
        if LooseVersion(version_wanted) > LooseVersion(version_installed):
            status = 'X'
    print('[{}] {:<11} {}'.format(
        status, pkg.ljust(13), version_installed)
        )
