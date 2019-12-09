import sys
from os import path

sys.path.insert(1, f"..{path.sep}..{path.sep}Data")
from getData import *

pull_data(4, 2019)
