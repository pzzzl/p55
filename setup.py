from distutils.core import setup
import py2exe

setup(
    # console=['p55.py'],
    windows = [{'script': 'p55.py'}],
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile = None
    )