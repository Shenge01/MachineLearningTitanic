import os

from ..config.config import PACKAGE_ROOT 

with open(os.path.join(PACKAGE_ROOT, 'VERSION')) as version_file:
	__version__ = version_file.read().strip()  ##set the version attribute