from distutils.core import setup
from glob import glob

from labyrinth_lib import __version__

setup(name='Labyrinth',
      version=__version__,
      description='',
      author='Labyrinth is a lightweight mind-mapping tool',
      author_email='Don@scorgie.org',
      url='http://people.gnome.org/~dscorgie/labyrinth.html',
      packages=['labyrinth_lib'],
      scripts=['labyrinth'],
      data_files=[('share/labyrinth', glob('data/*'))],
      requires=['PyGTK'],
      classifiers = [
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      ]
     )
